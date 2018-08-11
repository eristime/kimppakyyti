from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator


class Car(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cars',)
    model = models.CharField(max_length=50)
    register_plate = models.CharField(max_length=50)
    consumption = models.DecimalField(max_digits=4, decimal_places=2, default=None, validators=[MinValueValidator(0.01)]) #liters per 100 km

    def __str__(self):
        return self.owner.username + " - " + self.register_plate