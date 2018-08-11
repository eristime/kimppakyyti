from django.db import models

from apiv1.models.roles import Passenger
from apiv1.models.rides import DriverOnlyRide


class Request(models.Model):
    '''
    Passengers make a request to join the ride and driver accepts them. After that accepting, 
    a passenger is added and request deleted.
    '''

    STATUS = (
        ('PENDING', 'pending'),
        ('ACCEPTED', 'accepted'),
    )

    #TODO: check that there are no overlapping requests
    ride  = models.ForeignKey(DriverOnlyRide, on_delete=models.CASCADE, related_name='requests',)  
    requester = models.ForeignKey(Passenger, on_delete=models.CASCADE, related_name='requests',)
    note = models.TextField()
    status = models.CharField(max_length=10,choices=STATUS)

    def __str__(self):
        return self.id
