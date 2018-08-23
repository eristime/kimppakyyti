from django.test import TestCase
from django.contrib.auth.models import User

from apiv1.models.rides import Car

class CarModelTest(TestCase):

    def setUp(self):
        # Set up non-modified objects used by all test methods
        self.user = User.objects.create_user(
            username='test_user', password='some_secure_password here')
        Car.objects.create(owner=self.user, brand='Volvo', model='V60', registerplate='FXX-123', consumption=8.50)

    def test_brand_max_length(self):
        car = Car.objects.get(id=1)
        max_length = car._meta.get_field('brand').max_length
        self.assertEquals(max_length, 100)

    def test_model_max_length(self):
        car = Car.objects.get(id=1)
        max_length = car._meta.get_field('model').max_length
        self.assertEquals(max_length, 100)

    def test_register_plate_max_length(self):
        car = Car.objects.get(id=1)
        max_length = car._meta.get_field('register_plate').max_length
        self.assertEquals(max_length, 100)

    def test_consumption_max_digits(self):
        car = Car.objects.get(id=1)
        max_length = car._meta.get_field('consumption').max_digits
        self.assertEquals(max_digits, 4)

    def test_consumption_decimal_places(self):
        car = Car.objects.get(id=1)
        decimal_places = car._meta.get_field('consumption').decimal_places
        self.assertEquals(decimal_places, 2)

    def test_object_name(self):
        car = Car.objects.get(id=1)
        expected_object_name = f'User: {owner.id} car {car.first_name}'
        self.assertEquals(expected_object_name, str(car))

    def test_get_absolute_url(self):
        pass
        #TODO define nested resources first
        #car = Car.objects.get(id=1)
        # This will also fail if the urlconf is not defined.
        #self.assertEquals(car.get_absolute_url(), '/catalog/car/1')