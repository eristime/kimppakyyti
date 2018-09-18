from datetime import date, timedelta

from django.shortcuts import reverse
from django.contrib.auth.models import User, AnonymousUser

from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from rest_framework.test import force_authenticate
from rest_framework import status

from apiv1.models import Car, Ride, Profile


class TestRideList(APITestCase):

    def setUp(self):
        # create user objects
        self.user = User.objects.create_user(
            username='test_user', password='some_secure_password here')
        self.user_car = Car.objects.create(owner=self.user,\
                                        brand='Volvo', \
                                        model='V60', \
                                        register_plate='FXX-123',\
                                        consumption=8.50)
        #Profile.objects.create(owner=self.user, first_name='Mauno', last_name='Koivisto', phone_number='12345')
        self.user_ride_date = date.today() + timedelta(days=3)
        self.user_ride = Ride.objects.create(driver=self.user, \
                            car=self.user_car, \
                            destination='helsinki', \
                            departure='oulu', \
                            date=self.user_ride_date.__str__(), \
                            available_seats=3, \
                            total_seat_count=3, \
                            estimated_fuel_cost=15.5)

        # create another user objects
        self.another_user_ride_date = date.today() + timedelta(days=5) # rides on different day
        self.another_user = User.objects.create_user(
            username='another_user', password='some_ultra_secure_password here')
        self.another_user_car = Car.objects.create(owner=self.another_user,\
                                                   brand='Audi',\
                                                   model='R80XYZLOL',\
                                                   register_plate='SXX-123',\
                                                   consumption=30.50)
        #Profile.objects.create(owner=self.another_user, first_name='Urho', last_name='Kekkonen', phone_number='12345')            
        self.another_user_ride= Ride.objects.create(driver=self.another_user, \
                            car=self.another_user_car, \
                            destination='helsinki', \
                            departure='oulu', \
                            date=self.another_user_ride_date.__str__(), \
                            available_seats=3, \
                            total_seat_count=3, \
                            estimated_fuel_cost=15.5)


    def test_users_can_create_ride(self):
        '''
        Ensure it is possible to create a new ride object for authenticated users.
        '''
        # api won't allow creating objects if date passed so we set date to future
        date_for_input = date.today() + timedelta(days=3)
        data = {
            'car': self.user_car.pk,
            'destination': 'oulu',
            'departure': 'helsinki',
            'date': date_for_input.__str__(), # also api uses datetimes.date string representation
            'available_seats': 3,
            'estimated_fuel_cost': 12.00
        }
        
        url = reverse('ride-list')
        client = APIClient()
        client.force_authenticate(user=self.user)
        response = client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Ride.objects.count(), 3)


    def test_ride_status_is_set_on_creation(self):
        '''
        Ensure the ride status is automatically set to 'ONGOING' when creating a ride.
        '''
        # api won't allow creating objects if date passed so we set date to future
        date_for_input = date.today() + timedelta(days=3)
        data = {
            'car': self.user_car.pk,
            'destination': 'oulu',
            'departure': 'helsinki',
            'date': date_for_input.__str__(), # also api uses datetimes.date string representation
            'available_seats': 3,
            'estimated_fuel_cost': 12.00
        }
        
        url = reverse('ride-list')
        client = APIClient()
        client.force_authenticate(user=self.user)
        response = client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Ride.objects.count(), 3)
        self.assertEqual(Ride.objects.get(pk=self.user_ride.pk).status, Ride.ONGOING) # two ways of doing the same thing
        self.assertEqual(self.user_ride.status, Ride.ONGOING)


    def test_users_cannot_create_rides_using_other_users_cars(self):
        '''
        Ensure it's not possible to use other user's cars to post rides.
        '''

        date_for_input = date.today() + timedelta(days=3)
        data = {
            'car': self.another_user_car.pk,
            'destination': 'oulu',
            'departure': 'helsinki',
            'date': date_for_input.__str__(), # also api uses datetimes.date string representation
            'available_seats': 3,
            'estimated_fuel_cost': 12.00
        }
        url = reverse('ride-list')

        client = APIClient()
        client.force_authenticate(user=self.user)
        response = client.post(url, data, format='json')

        self.assertEqual(Ride.objects.count(), 2) # ride creation didn't work, only two rides
        self.assertEqual(response.status_code, 400) # API returns 400 since only user cars are returned using serializer


    def test_users_can_see_rides(self):
        '''
        Ensure authenticated users can see rides.
        '''

        client = APIClient()
        client.force_authenticate(user=self.user)

        url = reverse('ride-list')
        response = client.get(url, format='json')  
        
        self.assertEqual(len(response.data['results']), 2) # two rides overall, both on diffent dates
        self.assertEqual(response.status_code, 200)


    def test_users_can_filter_rides_using_date(self):
        '''
        Ensure authenticated users can only get a list of cars which belong to them.
        '''

        client = APIClient()
        client.force_authenticate(user=self.user)

        url = reverse('ride-list') + '?date=' + self.user_ride_date.__str__() # construct filter query

        response = client.get(url, format='json')  

        
        self.assertEqual(len(response.data['results']), 1) # two rides overall, both on diffent dates
        self.assertEqual(response.data['results'][0]['date'], self.user_ride_date.__str__())
        self.assertEqual(response.status_code, 200)

       
    def test_ride_list_view_available_for_unauthenticated_users(self):
        '''
        Ensure also unauthenticated users can see the rides.
        '''
        url = reverse('ride-list')
        date_for_input = date.today() + timedelta(days=3)
        data = {
            'car': self.user_car.pk,
            'destination': 'oulu',
            'departure': 'helsinki',
            'date': date_for_input.__str__(), # also api uses datetimes.date string representation
            'available_seats': 3,
            'estimated_fuel_cost': 12.00
        }
        
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, 401)
        self.assertEqual(Ride.objects.count(), 2) # ride creation didn't work, only two rides


        response = self.client.get(url, format='json')
        
        self.assertEqual(response.status_code, 200) # getting rides works
