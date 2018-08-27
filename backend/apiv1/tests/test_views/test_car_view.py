from django.shortcuts import reverse
from django.contrib.auth.models import User, AnonymousUser

from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from rest_framework.test import force_authenticate
from rest_framework import status

from apiv1.models import Car


class TestCar(APITestCase):

    def setUp(self):
        # create objects
        self.user = User.objects.create_user(
            username='test_user', password='some_secure_password here')
        # create a car user owns
        Car.objects.create(owner=self.user, brand='Volvo', model='V60', register_plate='FXX-123', consumption=8.50)
        # create someone else's car
        self.another_user = User.objects.create_user(
            username='another_user', password='some_ultra_secure_password here')
        Car.objects.create(owner=self.another_user, brand='Audi', model='R80XYZLOL', register_plate='SXX-123', consumption=30.50)


    def test_users_can_create_car(self):
        '''
        Ensure it is possible to create a new car object for authenticated users.
        '''
        url = reverse('car-list')
        data = { 'brand':'Saab', 'model':'92', 'register_plate':'kkk-555', 'consumption':10.50}
        
        client = APIClient()
        client.force_authenticate(user=self.user)
        response = client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Car.objects.count(), 3)
        #self.assertEqual(Car.objects.get().owner, self.user) TODO: is this line needed?


    def test_users_cannot_see_other_users_cars(self):
        '''
        Ensure authenticated users can only get a list of cars which belong to them.
        '''

        client = APIClient()
        client.force_authenticate(user=self.user)

        response = client.get(reverse('car-list'), format='json')
        
        # user has only one car
        self.assertEqual(len(response.data['results']), 1)
        
        self.assertEqual(response.status_code, 200)


    def test_car_list_view_not_available_for_unauthenticated_users(self):
        '''
        Ensure unauthenticated users can't use the car-list view.
        '''
        url = reverse('car-list')
        data = { 'brand':'Saab', 'model':'92', 'register_plate':'kkk-555', 'consumption':10.50}
        
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, 403)
        self.assertEqual(Car.objects.count(), 2)

        response = self.client.get(url, format='json')

        self.assertEqual(response.status_code, 403)


    def test_owner_can_see_car_details(self):
        '''
        Ensure owner can see her car details.
        '''
        client = APIClient()
        client.force_authenticate(user=self.user)

        # point url to current authenticated user car
        authenticated_user_car_pk = Car.objects.filter(owner=self.user)[0].pk
        url = reverse('car-detail', args=[authenticated_user_car_pk])

        response = client.get(url, format='json')
        
        self.assertEqual(200, response.status_code)


    def test_users_cant_see_others_car_details(self):
        '''
        Ensure it is not possible to see others cars
        '''
        client = APIClient()
        client.force_authenticate(user=self.user)

        # point url to other user car
        another_user_car_pk = Car.objects.filter(owner=self.another_user)[0].pk
        url = reverse('car-detail', args=[another_user_car_pk])

        response = client.get(url, format='json')
        
        self.assertEqual(403, response.status_code)


    def test_owner_can_delete_car(self):
        '''
        Ensure owner can delete her car.
        '''
        client = APIClient()
        client.force_authenticate(user=self.user)

        # point url to current authenticated user car
        authenticated_user_car_pk = Car.objects.filter(owner=self.user)[0].pk
        url = reverse('car-detail', args=[authenticated_user_car_pk])

        response = client.delete(url, format='json')
        

        self.assertEqual(Car.objects.count(), 1)
        self.assertEqual(204, response.status_code)


    def test_users_cant_delete_others_cars(self):
        '''
        Ensure it is not possible to delete someone else's car.
        '''
        client = APIClient()
        client.force_authenticate(user=self.user)

        # point url to other user car
        authenticated_user_car_pk = Car.objects.filter(owner=self.another_user)[0].pk
        url = reverse('car-detail', args=[authenticated_user_car_pk])

        response = client.delete(url, format='json')
        

        self.assertEqual(Car.objects.count(), 2)
        self.assertEqual(403, response.status_code)


    def test_car_detail_not_available_for_unauthenticated_users(self):
        '''
        Ensure that unauthenticated users are not able to interact with the endpoint.
        '''

        url = reverse('car-detail', args=[1])

        response = self.client.get(url, format='json')
        self.assertEqual(403, response.status_code)

        response = self.client.delete(url, format='json')
        self.assertEqual(403, response.status_code)