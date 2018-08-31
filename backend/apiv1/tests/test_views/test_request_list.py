from datetime import date, timedelta

from django.shortcuts import reverse
from django.contrib.auth.models import User, AnonymousUser

from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from rest_framework.test import force_authenticate
from rest_framework import status

from apiv1.models import Car, Ride, Request, Passenger


class TestRequestList(APITestCase):

    def setUp(self):
        # create objects
        self.user = User.objects.create_user(
            username='test_user', password='some_secure_password here')
        # create a ride user owns
        self.user_car = Car.objects.create(owner=self.user,\
                                        brand='Volvo', \
                                        model='V60', \
                                        register_plate='FXX-123',\
                                        consumption=8.50)
        
        # create a ride
        self.user_ride_date = date.today() + timedelta(days=3)
        self.user_ride = Ride.objects.create(driver=self.user, \
                            car=self.user_car, \
                            destination='helsinki', \
                            departure='oulu', \
                            date=self.user_ride_date.__str__(), \
                            available_seats=3, \
                            total_seat_count=3, \
                            estimated_fuel_cost=15.5)


        # create car for another user
        self.another_user_ride_date = date.today() + timedelta(days=5) # rides on different day
        self.another_user = User.objects.create_user(
            username='another_user', password='some_ultra_secure_password here')
        self.another_user_car = Car.objects.create(owner=self.another_user,\
                                                   brand='Audi',\
                                                   model='R80XYZLOL',\
                                                   register_plate='SXX-123',\
                                                   consumption=30.50)
        # create ride made by another user
        self.another_user_ride = Ride.objects.create(driver=self.another_user, \
                            car=self.another_user_car, \
                            destination='helsinki', \
                            departure='oulu', \
                            date=self.another_user_ride_date.__str__(), \
                            available_seats=3, \
                            total_seat_count=3, \
                            estimated_fuel_cost=15.5)

        # not possible to create a request for a ride where user acts as a driver
        #Request.objects.create(ride=self.user_ride, requester=self.another_user, note='lolz')
        #Request.objects.create(ride=self.another_user_ride, requester=self.user, note='xD')


    def test_users_can_create_request(self):
        '''
        Ensure it is possible to create a new request object.
        '''

        data = {
            'note': 'some_note'
        }
        client = APIClient()
        client.force_authenticate(user=self.user)

        # point url to another user request
        another_user_ride = Ride.objects.filter(driver=self.another_user)[0]
        url = reverse('request-list', args=[another_user_ride.pk])
        response = client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Request.objects.count(), 1)


    def test_users_cannot_create_request_for_ride_where_user_driver(self):
        '''
        Ensure it's not possible to create a request for a ride where user a driver.
        '''
        data = {
            'note': 'some_note'
        }
        client = APIClient()
        client.force_authenticate(user=self.user)

        # point url to user request
        user_ride = Ride.objects.filter(driver=self.user)[0]
        url = reverse('request-list', args=[user_ride.pk])
        response = client.post(url, data, format='json')

        self.assertEqual(response.status_code, 400)
        self.assertEqual(Request.objects.count(), 0)


    def test_users_cannot_create_requests_if_they_already_have_one(self):
        '''
        Ensure it's not possible to create a requests if users already have one to same ride.
        '''
        data = {
            'note': 'some_note'
        }
        # create a request 
        Request.objects.create(ride=self.another_user_ride, requester=self.user, note='lolz')
        client = APIClient()
        client.force_authenticate(user=self.user)

        # point url to another user request
        another_user_ride = Ride.objects.filter(driver=self.another_user)[0]
        url = reverse('request-list', args=[another_user_ride.pk])
        response = client.post(url, data, format='json')

        self.assertEqual(response.status_code, 400)
        self.assertEqual(Request.objects.count(), 1) # only one request available which we just created in this test


    def test_users_cannot_create_requests_if_user_already_passenger(self):
        '''
        Ensure it's not possible to create a request for a ride where user a driver.
        '''
        data = {
            'note': 'some_note'
        }
        client = APIClient()
        client.force_authenticate(user=self.user)

        
        # point url to another user request
        another_user_ride = Ride.objects.filter(driver=self.another_user)[0]
        Passenger.objects.create(user=self.user, ride=another_user_ride)

        url = reverse('request-list', args=[another_user_ride.pk])
        response = client.post(url, data, format='json')


        self.assertEqual(response.status_code, 400)
        self.assertEqual(Request.objects.count(), 0)


    def test_users_cant_create_requests_for_completed_rides(self):
        '''
        Ensure it is not possible to create requests for completed rides.
        '''
        data = {
            'note': 'some_note'
        }
        # create a ride and make it complete
        local_another_user_ride = Ride.objects.create(driver=self.another_user, \
                            car=self.another_user_car, \
                            destination='helsinki', \
                            departure='oulu', \
                            date=self.another_user_ride_date.__str__(), \
                            available_seats=3, \
                            total_seat_count=3, \
                            estimated_fuel_cost=15.5)
        #setattr(local_another_user_ride, 'status', 'COMPLETED')
        #local_another_user_ride.save()
        
        local_another_user_ride.status='COMPLETED'
        local_another_user_ride.save()

        client = APIClient()
        client.force_authenticate(user=self.user)

        
        # point url to another user request
        url = reverse('request-list', args=[local_another_user_ride.pk])
        response = client.post(url, data, format='json')


        self.assertEqual(response.status_code, 400)
        self.assertEqual(Request.objects.count(), 0)



    def test_non_drivers_cant_see_requests(self):
        '''
        Ensure non drivers can't see requests.
        '''
        REQUEST_1_NOTE = 'lolz'
        Request.objects.create(ride=self.another_user_ride, requester=self.user, note=REQUEST_1_NOTE)
        client = APIClient()
        client.force_authenticate(user=self.user)

        # point url to another user request
        another_user_ride = Ride.objects.filter(driver=self.another_user)[0]
        url = reverse('request-list', args=[another_user_ride.pk])

        response = client.get(url, format='json')
        
        self.assertEqual(len(response.data['results']), 0) # no requests returned
        self.assertEqual(response.status_code, 200)


    def test_drivers_can_see_requests_for_their_ride(self):
        '''
        Ensure drivers able to get correct number of requests.
        '''
        REQUEST_1_NOTE = 'lolz'
        Request.objects.create(ride=self.user_ride, requester=self.another_user, note=REQUEST_1_NOTE)
        Request.objects.create(ride=self.another_user_ride, requester=self.user, note='xD')
        client = APIClient()
        client.force_authenticate(user=self.user)

        # point url to user request
        user_ride = Ride.objects.filter(driver=self.user)[0]
        url = reverse('request-list', args=[user_ride.pk])

        response = client.get(url, format='json')
        
        self.assertEqual(len(response.data['results']), 1) # two requests overall, one for user_ride
        self.assertEqual(response.data['results'][0]['note'], REQUEST_1_NOTE)
        self.assertEqual(response.status_code, 200)


    def test_ride_list_view_not_available_for_unauthenticated_users(self):
        '''
        Ensure unauthenticated users can't use the request-list view.
        '''
        data = {
            'note': 'some_note'
        }
        
        # point url to another user request
        another_user_ride = Ride.objects.filter(driver=self.another_user)[0]
        url = reverse('request-list', args=[another_user_ride.pk])

        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, 401)
        self.assertEqual(Request.objects.count(), 0) # request creation didn't work, only two rides

        response = self.client.get(url, format='json')

        self.assertEqual(response.status_code, 401)
