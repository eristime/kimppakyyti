from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework import generics

from apiv1.models import Ride
from apiv1.serializers import RideSerializer


class UserRidesAsDriverList(generics.ListAPIView):
    ''' Only logged in user able to see her rides where she acts as a driver'''
    permission_classes = (permissions.IsAuthenticated, )
    serializer_class = RideSerializer


    def get_queryset(self):
        """
        This should return all rides where user acts as a driver.
        """

        if self.request.user.is_anonymous:
            return Ride.objects.none()

        return Ride.objects.filter(driver=self.request.user)
    