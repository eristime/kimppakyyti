from rest_framework import generics

from apiv1.serializers import EndRideSerializer
from apiv1.permissions import IsDriver
from apiv1.models import Ride


class EndRide(generics.UpdateAPIView):
    '''Only driver able to modify.'''
    permission_classes = (IsDriver,) 
    queryset = Ride.objects.all()
    serializer_class = EndRideSerializer


    def perform_update(self, serializer):
        serializer.save(status=Ride.COMPLETED)
