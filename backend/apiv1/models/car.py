from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator


class Car(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cars',)
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    register_plate = models.CharField(max_length=100)
    consumption = models.DecimalField(max_digits=4, decimal_places=2, null=True, validators=[MinValueValidator(0.01)]) #liters per 100 km

    def __str__(self):
        return "User: " + str(self.owner.id) + " car " + self.register_plate