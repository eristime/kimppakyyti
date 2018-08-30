from django.db import models
from django.contrib.auth.models import User
from apiv1.models import Ride


class Passenger(models.Model):
    '''Rides have passengers. Passenger is a user who isn't a driver'''
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='passenger',)
    ride = models.ForeignKey(Ride, on_delete=models.CASCADE, related_name='passenger',)
    #rating = models.DecimalField(max_digits=3, decimal_places=2, default=None) # modify to 0 - 5 scale
    #review_count = models.PositiveIntegerField(default=0)  
    # TODO add comments for reviews


    def __str__(self):
        return str(self.user.id)
