from django.db import models

from apiv1.models.rides import Ride
from django.contrib.auth.models import User


class Request(models.Model):
    '''
    Passengers make a request to join the ride and driver accepts them. After that accepting, 
    a passenger is added and request deleted.
    '''
    PENDING = 'PENDING'
    ACCEPTED = 'ACCEPTED'
    STATUS = (
        (PENDING, 'pending'),
        (ACCEPTED, 'accepted'),
    )

    #request_id = models.AutoField(primary_key=True)
    ride  = models.ForeignKey(Ride, on_delete=models.CASCADE, related_name='requests',)  
    requester = models.ForeignKey(User, on_delete=models.CASCADE, related_name='requests',)
    note = models.TextField()
    status = models.CharField(max_length=10,choices=STATUS)

    def __str__(self):
        return "Request " + str(self.id)


    def save(self, *args, **kwargs):
        self.status = self.PENDING
        return super(Request, self).save(*args, **kwargs)