from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile',)
    
    #private
    reported = models.IntegerField(default=0)  # not in use
    deleted = models.BooleanField(default=False) # not in use
    is_active = models.BooleanField(default=True) # not in use
    token = models.CharField(max_length=100, unique=True)  # TODO: find a better place

    # public
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=1000, default=None) 
    photo = models.CharField(max_length=50, default=None) # URL for picture

    driver_rating = models.DecimalField(max_digits=3, decimal_places=2, default=None) # modify to 0 - 5 scale
    driver_reviews = models.IntegerField(default=0)
    passenger_rating = models.DecimalField(max_digits=3, decimal_places=2, default=None) # modify to 0 - 5 scale
    passenger_reviews = models.IntegerField(default=0)
    
    def __str__(self):
        return self.first_name + " - " + self.last_name + " profile"


class Car(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cars',)
    model = models.CharField(max_length=50)
    register_plate = models.CharField(max_length=50)
    consumption = models.DecimalField(max_digits=4, decimal_places=2, default=None) #liters per 100 km

    def __str__(self):
        return self.owner.username + " - " + self.register_plate

#class Passenger:
#    '''Rides have passengers. Passenger is a user who isn't a driver'''
#    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='passenger',)
#    ride = models.ForeignKey(Ride, on_delete=models.CASCADE, related_name='passenger',)

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

    private = models.OneToOneField(PrivateRide, on_delete=models.CASCADE, related_name='profile',)
    driver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='rides',)
    # only passenger information not available to public
    passengers = models.ManyToManyField(User, verbose_name="passengers", default=None)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)  # probably not want to delete when deleting a car

    destination = models.CharField(max_length=50)
    departure = models.CharField(max_length=50)
    available_seats = models.IntegerField()
    status = models.CharField(max_length=10,choices=STATUS)
    
    #ride_ended = models.DateTimeField(default=None) #TODO fix the fault
    
    estimated_fuel_cost = models.DecimalField(max_digits=6, decimal_places=2)
    recurrent = models.CharField(max_length=1,choices=RECURRENCY, default='ONE_TIME')  # not in use
    
    
    ## implemented if time 
    #Route Object
    #[‘rovaniemi’, ‘tervola’, ‘kemi’, ‘ii’, ‘oulu’]
    #Pick-up location

    def __str__(self):
        return self.departure + " - " + self.destination


class PrivateRide(models.Model):
    #

class Message(models.Model):

    ride  = models.ForeignKey(Ride, on_delete=models.CASCADE, related_name='messages',)  # deleteting messages when ride deleted
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages',) # cascading??
    # if empty, it is a group message for all participants in the ride
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages',) # cascading??
    body = models.TextField()
    timestamp = models.DateTimeField()
    inappropriate = models.BooleanField(default=False)

    def __str__(self):
        return self.id



# additional feature
class Route(models.Model):
    #Ride ID
    #Route
    #Origin_city
    #Destination_city
    #Origin_coordinates
    #Destination_coordinates
    pass

    #def __str__(self):
    #    return self.ride + " - " + self.sender