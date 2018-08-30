from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from django.db.models.signals import post_save
from django.dispatch import receiver

from apiv1.models.car import Car


class Ride(models.Model):
    
    ONGOING = 'ONGOING'
    COMPLETED = 'COMPLETED'

    STATUS = (
        (ONGOING, 'ongoing'),
        (COMPLETED, 'completed'),
    )
    ONE_TIME = 'ONE_TIME'
    DAILY = 'DAILY'
    WEEKLY = 'WEEKLY'
    MONTHLY = 'MONTHLY'


    RECURRENCY = (
        ('ONE_TIME', 'one_time'),
        ('DAILY', 'daily'),
        ('WEEKLY', 'weekly'),
        ('MONTHLY', 'monthly'),
    )

    
    #driver_only = models.OneToOneField(DriverOnlyRide, on_delete=models.CASCADE, related_name='ride',)
    driver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='rides',)

    
    # TODO don't cascade delete but lock it instead
    car = models.ForeignKey(Car, on_delete=models.CASCADE,) 

    destination = models.CharField(max_length=50)
    departure = models.CharField(max_length=50)
    date = models.DateField()
    available_seats = models.PositiveIntegerField()
    total_seat_count = models.PositiveIntegerField()
    status = models.CharField(max_length=10,choices=STATUS, default=ONGOING, editable=False)
    estimated_fuel_cost = models.DecimalField(max_digits=6, decimal_places=2, validators=[MinValueValidator(0.01)], blank=True)
    recurrent = models.CharField(max_length=1,choices=RECURRENCY, default='one_time')  # not in use

    
    ## implemented if time 
    #Route Object
    #[‘rovaniemi’, ‘tervola’, ‘kemi’, ‘ii’, ‘oulu’]
    #Pick-up location

    def __str__(self):
        return "Ride: " + str(self.id) + " from" + self.departure + " to " + self.destination

    def save(self, *args, **kwargs):
        self.destination = self.destination.lower()
        self.departure = self.departure.lower()
        self.total_seat_count = self.available_seats # check if this works
        self.status = self.ONGOING
        return super(Ride, self).save(*args, **kwargs)



class PrivateRide(models.Model):
    '''Extend Ride-model with information only available to participants.'''
    ride = models.OneToOneField(Ride, on_delete=models.CASCADE, related_name='private_ride',)
    passengers = models.ManyToManyField(User, verbose_name="passengers", related_name='passengers', blank=True)
    #messages = models.ForeignKey(GroupMessage, on_delete=models.CASCADE, related_name='group_messages',) # will cause the loop

    def __str__(self):
        return self.ride.id + " - private ride"



class DriverOnlyRide(models.Model):
    '''Extend Ride-model with information only available to driver.'''
    #TODO handle the case of not 
    #requests = models.ForeignKey(Request, on_delete=models.SET_NULL, related_name='ride',)
    #messages
    #
    ride = models.OneToOneField(Ride, on_delete=models.CASCADE, related_name='driver_only_ride',)

    def __str__(self):
        return self.ride.id + " - driver only ride"



class StaffOnlyRide(models.Model):
    '''Extend Ride-model with fields which are only available to staff. '''
    #TODO handle the case of not 
    #requests = models.ForeignKey(Request, on_delete=models.SET_NULL, related_name='ride',)
    #messages
    #
    ride = models.OneToOneField(Ride, on_delete=models.CASCADE, related_name='staff_only_ride',)

    def __str__(self):
        return self.ride.id + " - staff only ride"



#TODO add first and last_name automatically
@receiver(post_save, sender=Ride)
def create_rides(sender, instance, created, **kwargs):
    if created:
        PrivateRide.objects.create(ride=instance)
        DriverOnlyRide.objects.create(ride=instance)
        StaffOnlyRide.objects.create(ride=instance)