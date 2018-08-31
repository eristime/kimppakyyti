from datetime import date, timedelta
from django.shortcuts import reverse
from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from rest_framework.test import force_authenticate
from rest_framework import status

from apiv1.models import Ride, Car, Request


class TestRequestDetail(APITestCase):

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

        Request.objects.create(ride=self.user_ride, requester=self.user, note='lolz')
        Request.objects.create(ride=self.another_user_ride, requester=self.another_user, note='xD')


    def test_requester_can_see_her_request_details(self):
        '''
        Ensure requester can see her request details.
        '''
        client = APIClient()
        client.force_authenticate(user=self.user)

        # point url to user request
        user_ride = Ride.objects.filter(driver=self.user)[0]
        user_request = Request.objects.filter(requester=self.user, ride=user_ride)[0]
        url = reverse('request-detail', args=[user_ride.pk, user_request.pk])

        response = client.get(url, format='json')
        #print('response_data:', response.data)
        
        self.assertEqual(200, response.status_code)


    def test_users_cant_see_others_request_details(self):
        '''
        Ensure it is not possible to see others requests
        '''
        client = APIClient()
        client.force_authenticate(user=self.user)

        # point url to other user request
        another_user_ride = Ride.objects.filter(driver=self.another_user)[0]
        another_user_request = Request.objects.filter(requester=self.another_user, ride=another_user_ride)[0]
        url = reverse('request-detail', args=[another_user_ride.pk, another_user_request.pk])

        response = client.get(url, format='json')
        
        self.assertEqual(403, response.status_code)


    def test_requester_can_delete_her_request(self):
        '''
        Ensure requester can delete her request.
        '''
        client = APIClient()
        client.force_authenticate(user=self.user)

        # point url user request
        user_ride = Ride.objects.filter(driver=self.user)[0]
        user_request = Request.objects.filter(requester=self.user, ride=user_ride)[0]
        url = reverse('request-detail', args=[user_ride.pk, user_request.pk])

        response = client.delete(url, format='json')
        self.assertEqual(Request.objects.count(), 1)  # two request overall, now one deleted
        self.assertEqual(204, response.status_code)


    def test_users_cant_delete_others_requests(self):
        '''
        Ensure it is not possible to delete someone else's request.
        '''
        client = APIClient()
        client.force_authenticate(user=self.user)

        # point url to other user request
        another_user_ride = Ride.objects.filter(driver=self.another_user)[0]
        another_user_request = Request.objects.filter(requester=self.another_user, ride=another_user_ride)[0]
        url = reverse('request-detail', args=[another_user_ride.pk, another_user_request.pk])

        response = client.delete(url, format='json')
        
        self.assertEqual(Request.objects.count(), 2)  # two requests overall, deletion didn't complete
        self.assertEqual(403, response.status_code)


    def test_requester_can_update_her_request_note(self):
        '''
        Ensure requester can update her request note.
        '''
        NEW_NOTE = 'this is a new note'
        data = {
            'note': NEW_NOTE
        }
        client = APIClient()
        client.force_authenticate(user=self.user)

       # point url user request
        user_ride = Ride.objects.filter(driver=self.user)[0]
        user_request = Request.objects.filter(requester=self.user, ride=user_ride)[0]
        url = reverse('request-detail', args=[user_ride.pk, user_request.pk])

        response = client.patch(url, data, format='json')
        
        self.assertEqual(Request.objects.count(), 2)  # two requests still
        self.assertEqual(200, response.status_code)
        self.assertEqual(response.data['note'], NEW_NOTE)


    def test_users_cant_update_others_request_notes(self):
        '''
        Ensure it is not possible to update someone else's request note.
        '''
        NEW_NOTE = 'this is a new note'
        data = {
            'note': NEW_NOTE
        }
        client = APIClient()
        client.force_authenticate(user=self.user)

        # point url to other user request
        another_user_ride = Ride.objects.filter(driver=self.another_user)[0]
        another_user_request = Request.objects.filter(requester=self.another_user, ride=another_user_ride)[0]
        url = reverse('request-detail', args=[another_user_ride.pk, another_user_request.pk])

        response = client.patch(url, data, format='json')
        
        self.assertEqual(Request.objects.count(), 2)  # two requests overall still
        self.assertEqual(403, response.status_code)


    def test_request_detail_not_available_for_unauthenticated_users(self):
        '''
        Ensure that unauthenticated users are not able to interact with the endpoint.
        '''

        user_ride = Ride.objects.filter(driver=self.user)[0]
        user_request = Request.objects.filter(requester=self.user, ride=user_ride)[0]
        url = reverse('request-detail', args=[user_ride.pk, user_request.pk])

        response = self.client.get(url, format='json')
        self.assertEqual(401, response.status_code)

        response = self.client.delete(url, format='json')
        self.assertEqual(401, response.status_code)