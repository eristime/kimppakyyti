from datetime import date, timedelta
from django.shortcuts import reverse
from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from rest_framework.test import force_authenticate
from rest_framework import status

from apiv1.models import Ride, Car


class TestCarDetail(APITestCase):

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
        Ride.objects.create(driver=self.user, \
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
        Ride.objects.create(driver=self.another_user, \
                            car=self.another_user_car, \
                            destination='helsinki', \
                            departure='oulu', \
                            date=self.another_user_ride_date.__str__(), \
                            available_seats=3, \
                            total_seat_count=3, \
                            estimated_fuel_cost=15.5)


    def test_owner_can_see_ride_details(self):
        '''
        Ensure ride-details can be seen.
        '''
        client = APIClient()
        client.force_authenticate(user=self.user)

        url = reverse('ride-detail', args=[1])

        response = client.get(url, format='json')
        
        self.assertEqual(200, response.status_code)


    def test_ride_detail_not_available_for_unauthenticated_users(self):
        '''
        Ensure that unauthenticated users are not able to interact with the endpoint.
        '''

        url = reverse('ride-detail', args=[1])

        response = self.client.get(url, format='json')
        self.assertEqual(403, response.status_code)
