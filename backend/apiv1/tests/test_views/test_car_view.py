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
        another_user = User.objects.create_user(
            username='another_user', password='some_ultra_secure_password here')
        Car.objects.create(owner=another_user, brand='Audi', model='R80XYZLOL', register_plate='SXX-123', consumption=30.50)


    def test_authenticated_users_can_create_car(self):
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


    def test_non_authenticated_users_cannot_create_car(self):
        '''
        Ensure non-authenticated users can't create cars.
        '''
        url = reverse('car-list')
        data = { 'brand':'Saab', 'model':'92', 'register_plate':'kkk-555', 'consumption':10.50}
        
        #client = APIClient()
        #client.force_authenticate(user=AnonymousUser)
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, 403)
        self.assertEqual(Car.objects.count(), 2)


    def test_authenticated_users_can_see_only_their_cars(self):
        '''
        Ensure authenticated users can only get a list of cars which belong to them.
        '''

        client = APIClient()
        client.force_authenticate(user=self.user)

        response = self.client.get(reverse('car-list'), format="json")
        
        # user has only one car
        self.assertEqual(len(response.data), 1)


#    def test_owner_can_update_car(self):
#        data = { 'brand':'BMW', 'model':'89', 'register_plate':'fff-888', 'consumption':6}
#
#        client = APIClient()
#        client.force_authenticate(user=self.user)
#        response = client.post(url, data, format='json')
#        response = self.client.put(reverse('car-detail', data, format="json")
#
#        # check info returned has the update
#        self.assertEqual('The Space Between Us updated', response.data['name'])


    def test_owner_can_delete_car(self):
        '''Ensure owner can delete her car.'''
        client = APIClient()
        client.force_authenticate(user=self.user)
        url = reverse("car-detail", args=[self.user.pk])

        response = client.delete(url, format="json")
        

        self.assertEqual(Car.objects.count(), 1)
        self.assertEqual(204, response.status_code)
