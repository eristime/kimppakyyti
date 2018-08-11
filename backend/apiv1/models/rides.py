from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator

from apiv1.models.roles import Passenger, Driver
from apiv1.models.car import Car




class PrivateRide(models.Model):
    '''Only ride participants can see and modify.'''
    passengers = models.ManyToManyField(Passenger, verbose_name="passengers", related_name='passengers',default=None)
    #messages = models.ForeignKey(GroupMessage, on_delete=models.CASCADE, related_name='group_messages',) # will cause the loop


class DriverOnlyRide(models.Model):
    '''Only driver can add passengers. '''
    #TODO handle the case of not 
    #requests = models.ForeignKey(Request, on_delete=models.SET_NULL, related_name='ride',)
    #messages
    #
    something = models.CharField(max_length=4)

    def __str__(self):
        return "something"


class Ride(models.Model):

    STATUS = (
        ('ONGOING', 'ongoing'),
        ('COMPLETED', 'completed'),
    )

    RECURRENCY = (
        ('ONE_TIME', 'one_time'),
        ('DAILY', 'daily'),
        ('WEEKLY', 'weekly'),
        ('MONTHLY', 'MONTHLY'),
    )

    private = models.OneToOneField(PrivateRide, on_delete=models.CASCADE, related_name='ride',)
    driver_only = models.OneToOneField(DriverOnlyRide, on_delete=models.CASCADE, related_name='ride',)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE, related_name='rides',)

    
    # TODO don't cascade delete but lock it instead
    car = models.ForeignKey(Car, on_delete=models.CASCADE) 

    destination = models.CharField(max_length=50)
    departure = models.CharField(max_length=50)
    available_seats = models.PositiveIntegerField()
    status = models.CharField(max_length=10,choices=STATUS)
    
    #ride_ended = models.DateTimeField(default=None) #TODO fix the fault
    
    estimated_fuel_cost = models.DecimalField(max_digits=6, decimal_places=2, validators=[MinValueValidator(0.01)])
    recurrent = models.CharField(max_length=1,choices=RECURRENCY, default='ONE_TIME')  # not in use
    
    ## implemented if time 
    #Route Object
    #[‘rovaniemi’, ‘tervola’, ‘kemi’, ‘ii’, ‘oulu’]
    #Pick-up location

    def __str__(self):
        return self.departure + " - " + self.destination
