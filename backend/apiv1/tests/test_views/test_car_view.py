# cars-api/cars/api/tests/test_views.py

from django.shortcuts import reverse

from rest_framework.test import APITestCase
from rest_framework.test import force_authenticate
from rest_framework.test import APIRequestFactory

from api.models import Car


class TestCar(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='test_user', password='some_secure_password here')
        Car.objects.create(owner=self.user, brand='Volvo', model='V60', register_plate='FXX-123', consumption=8.50)


    def test_create_car(self):
        factory = APIRequestFactory()
        force_authenticate(request, user=self.user)
        request = factory.post('/cars/', { brand='Saab', model='92', register_plate='kkk-555', consumption=10.50}, format='json')

        # assert new car was added
        self.assertEqual(Car.objects.count(), 2)

        # assert a created status code was returned
        self.assertEqual(201, response.status_code)

    def test_getting_cars(self):
        response = self.client.get(reverse('cars'), format="json")
        self.assertEqual(len(response.data), 1)

    def test_updating_car(self):
        response = self.client.put(reverse('detail', kwargs={'pk': 1}), {
            'name': 'The Space Between Us updated',
            'year_of_release': 2017
        }, format="json")

        # check info returned has the update
        self.assertEqual('The Space Between Us updated', response.data['name'])

    def test_deleting_car(self):
        response = self.client.delete(reverse('detail', kwargs={'pk': 1}))

        self.assertEqual(204, response.status_code)


class UserAPITestCase(TestCase):

    """
    User API
    """

    def setUp(self):
        self.c = APIClient()

        self.normal_user = User.objects.create_user(
            username="joe", password="password", email="joe@soap.com")
        self.superuser = User.objects.create_superuser(
            username="clark", password="supersecret", email="joe@soap.com")

    def test_get_list_requires_login(self):
        """GET /user requires a logged in user"""
        url = reverse("user-list")
        response = self.c.get(url)

        assert response.status_code == 403, \
            "Expect 403 OK. got: {}" . format(response.status_code)
        num_users = len(response.json())

    def test_logged_in_user_can_get_list(self):
        """GET /user returns a list of users for a valid logged in user"""
        
        self.c.login(username="joe", password="password")
        url = reverse("user-list")
        response = self.c.get(url)

        assert response.status_code == 200, \
            "Expect 403. got: {}" . format(response.status_code)
        num_users = len(response.json())  
        assert num_users == 2, \
          'Expect exactly 2 users. Got: {}' . format (num_users)      


    def test_logged_in_user_can_view_self(self):
        """GET /user/{pk} works if a user is logged in"""

        self.c.login(username="joe", password="password", email="joe@soap.com")
        url = reverse("user-detail", args=[self.normal_user.pk])
        response = self.c.get(url)

        assert response.status_code == 200, \
            "Expect 200 OK. got: {}" . format(response.status_code)

    def test_logged_in_user_can_edit_self(self):
        """GET /user/{pk} A user should be able to edit their own details"""

        self.c.login(username="joe", password="password")
        url = reverse("user-detail", args=[self.normal_user.pk])

        data = {
            "username": "joe",
            "first_name": "Joe", 
            "last_name": "Soap",
        }

        response = self.c.put(url, data, format="json")

        assert response.status_code == 200, \
            "Expect 200 OK. got: {}: {}" . format(response.status_code, response.content)

        joe = User.objects.get(username="joe")
        
        assert joe.first_name == "Joe", \
            "Expect user's first_name to be Joe. Got: {}" . format(joe.first_name)
        
    def test_cannot_view_user_detail_of_different_user(self):
        """A user should not be able to get details of another user"""

        # login as joe:
        self.c.login(username="joe", password="password")
        # get clark's details
        url = reverse("user-detail", args=[self.superuser.pk])
        response = self.c.get(url)

        assert response.status_code == 403, \
            "Expect not to be able to view another user's details. Expected 403. Got: {}" . format (response.status_code)


    def test_get_user_requires_login(self):
        """GET /user/{pk} returns 403 for non-loggedin user"""

        url = reverse("user-detail", args=[self.normal_user.pk])
        response = self.c.get(url)

        assert response.status_code == 403, \
            "Expect 403. got: {}" . format(response.status_code)
       
    def test_cannot_create_user_if_not_logged_in(self):
        """POST /user/ returns 401 AUTHENTICATIOD REQUIRED if not logged in"""

        data = {
            "username": "joe2",
            "email": "joe2@soap.com",
            "password": "pass"
        }
        url = reverse("user-list")
        response = self.c.post(url, data)
        assert response.status_code == 403, \
            "Expect 403 AUTHENTICATION REQUIRED. got: {}" . format(
                response.status_code)
        assert User.objects.count() == 2, \
            'Expect no new users to have been created'

    def test_only_staff_can_create_user(self):
        """POST /user/ returns 403 AUTHENTICATIOD REQUIRED for 
a logged in user who is not superuser"""

        data = {
            "username": "joe2",
            "email": "joe2@soap.com",
            "password": "pass"
        }
        url = reverse("user-list")

        self.c.login(username="joe", password="password")
        response = self.c.post(url, data)

        assert response.status_code == 403, \
            'Expect 403 created. Got: {}' . format (response.status_code)
        
        assert User.objects.count() == 2, \
            'Expect no new users to have been created'


    def test_can_create_user_if_logged_in(self):
        """POST /user/ returns 201 CREATED for a valid logged in user"""

        data = {
            "username": "joe2",
            "email": "joe2@soap.com",
            "password": "pass"
        }
        url = reverse("user-list")

        self.c.login(username="clark", password="supersecret")
        response = self.c.post(url, data)

        assert response.status_code == 201, \
            'Expect 201 created. Got: {}' . format (response.status_code)

        assert User.objects.count() == 3, \
            'Expect a new user to have been created'

    def tearDown(self):
        for user in User.objects.all():
            user.delete()