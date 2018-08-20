from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework import generics

from apiv1.models import Ride, Passenger
from apiv1.serializers import RideSerializer


class UserRidesAsPassengerList(generics.ListAPIView):
    ''' Only logged in user able to see her rides where she is a passenger'''
    permission_classes = (permissions.IsAuthenticated, )
    serializer_class = RideSerializer


    def get_queryset(self):
        """
        This should return all rides in which user has participated as passenger.
        """

        if self.request.user.is_anonymous:
            return Ride.objects.none()


        rides = []
        # get all ride id's where user passenger
        for passenger in Passenger.objects.filter(user=self.request.user):
            rides.append(passenger.ride)

        return rides
    