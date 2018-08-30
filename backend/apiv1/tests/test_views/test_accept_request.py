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
        self.USER_RIDE_AVAILABLE_SEATS = 3
        self.user_ride_date = date.today() + timedelta(days=3)
        self.user_ride = Ride.objects.create(driver=self.user, \
                            car=self.user_car, \
                            destination='helsinki', \
                            departure='oulu', \
                            date=self.user_ride_date.__str__(), \
                            available_seats=self.USER_RIDE_AVAILABLE_SEATS, \
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
        Request.objects.create(ride=self.user_ride, requester=self.another_user, note='lolz')
        Request.objects.create(ride=self.another_user_ride, requester=self.user, note='xD')


    def test_drivers_can_accept_request(self):
        '''
        Ensure drivers can accept requests. 
        Also check that requester has been added as a passenger, ride available seats has been reduced by one
        and that the initial request is removed.
        '''

        client = APIClient()
        client.force_authenticate(user=self.user)

        # point url to user request
        another_user_request = Request.objects.filter(requester=self.another_user, ride=self.user_ride)[0]
        url = reverse('accept-request', args=[self.user_ride.pk, another_user_request.pk])

        response = client.post(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # check ride has now a new passenger
        self.assertEqual(True, Passenger.objects.filter(user=self.another_user, ride=self.user_ride).exists())

        # check available_seats has been decreased by one
        self.assertEqual(self.USER_RIDE_AVAILABLE_SEATS - 1, Ride.objects.get(pk=self.user_ride.pk).available_seats)

        # check that the initial request is now removed
        self.assertEqual(False, Request.objects.filter(requester=self.another_user, ride=self.user_ride).exists())


    def test_non_drivers_cant_accept_requests(self):
        '''
        Ensure non drivers can't accept requests.
        '''
        REQUEST_1_NOTE = 'lolz'
        Request.objects.create(ride=self.another_user_ride, requester=self.user, note=REQUEST_1_NOTE)
        client = APIClient()
        client.force_authenticate(user=self.another_user)
 
        # point url to another user request
        another_user_request = Request.objects.filter(requester=self.another_user, ride=self.user_ride)[0]
        url = reverse('accept-request', args=[self.user_ride.pk, another_user_request.pk])

        response = client.post(url, format='json')
        
        self.assertEqual(response.status_code, 403)


    def test_cant_accept_requests_if_no_available_seats(self):
        '''
        Ensure it is not possible to accept requests if no seats available for the ride.
        '''
        user_ride_no_seats = Ride.objects.create(driver=self.user, \
                            car=self.user_car, \
                            destination='helsinki', \
                            departure='oulu', \
                            date=self.user_ride_date.__str__(), \
                            available_seats=0, \
                            total_seat_count=3, \
                            estimated_fuel_cost=15.5)
        another_user_request = Request.objects.create(ride=user_ride_no_seats, requester=self.another_user, note='xD')
        
        client = APIClient()
        client.force_authenticate(user=self.user)

        # point url to user request
        another_user_request = Request.objects.get(requester=self.another_user, ride=user_ride_no_seats)
        url = reverse('accept-request', args=[user_ride_no_seats.pk, another_user_request.pk])

        response = client.post(url, format='json')
        self.assertEqual(response.status_code, 400)

    
    def test_cant_accept_requests_if_requester_already_passenger(self):
        '''
        Not implemented since the situation should never arise. Already tested when creating request.
        '''
        user_ride_no_seats = Ride.objects.create(driver=self.user, \
                            car=self.user_car, \
                            destination='helsinki', \
                            departure='oulu', \
                            date=self.user_ride_date.__str__(), \
                            available_seats=0, \
                            total_seat_count=3, \
                            estimated_fuel_cost=15.5)
        Passenger(user=self.another_user, ride=user_ride_no_seats)
        another_user_request = Request.objects.create(ride=user_ride_no_seats, requester=self.another_user, note='xD')
        
        client = APIClient()
        client.force_authenticate(user=self.user)

        # point url to user request
        another_user_request = Request.objects.get(requester=self.another_user, ride=user_ride_no_seats)
        url = reverse('accept-request', args=[user_ride_no_seats.pk, another_user_request.pk])

        response = client.post(url, format='json')
        self.assertEqual(response.status_code, 400)

    
    def test_cant_accept_requests_for_rides_which_dont_exist(self):
        '''
        Ensure it is not possible to accept requests for rides which dont exist.
        '''
        # this doesn't make sense to do since requests can only live inside a ride

    
    def test_cant_accept_requests_for_completed_rides(self):
        '''
        Ensure it is not possible to accept requests for completed rides.
        '''
        # more reasonable to test when creating a request in a first place


    def test_accept_request_view_not_available_for_unauthenticated_users(self):
        '''
        Ensure unauthenticated users can't use the accept-request view.
        '''
        
        # point url to another user request
        another_user_request = Request.objects.filter(requester=self.another_user, ride=self.user_ride)[0]
        url = reverse('accept-request', args=[self.user_ride.pk, another_user_request.pk])

        response = self.client.post(url, format='json')

        self.assertEqual(response.status_code, 403)
        self.assertEqual(Request.objects.count(), 2) # only two requested which were created in setup

        response = self.client.get(url, format='json')

        self.assertEqual(response.status_code, 403)
