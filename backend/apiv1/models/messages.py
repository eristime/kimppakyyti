from django.db import models
from django.contrib.auth.models import User
from apiv1.models.rides import PrivateRide, Ride


class GroupMessage(models.Model):

    ride  = models.ForeignKey(PrivateRide, on_delete=models.CASCADE, related_name='group_messages',)  # deleting messages when ride deleted
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    inappropriate = models.BooleanField(default=False)

    def __str__(self):
        return self.id


class Message(models.Model):

    ride  = models.ForeignKey(Ride, on_delete=models.CASCADE, related_name='messages',)  # deleteting messages when ride deleted
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages',) # cascading??
    # if empty, it is a group message for all participants in the ride
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages',) # cascading??
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    inappropriate = models.BooleanField(default=False)

    def __str__(self):
        return self.id
