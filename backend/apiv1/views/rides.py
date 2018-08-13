from rest_framework import permissions, generics

from apiv1.serializers import RideSerializer, PrivateRideSerializer
from apiv1.permissions import IsOwnerOrReadOnly
from apiv1.models import Ride, PrivateRide, DriverOnlyRide

class RideDetail(generics.RetrieveUpdateDestroyAPIView):
    '''All able to see. Only driver able to modify.'''
    permission_classes = (IsOwnerOrReadOnly)
    serializer_class = RideSerializer

    #def get_queryset(self):
    #    return Ride.objects.all().filter(user=self.request.user)


class RideList(generics.ListCreateAPIView):
    '''All able to see. Drivers with cars able to post. (done automatically?)'''
    #only drivers who have cars able to create a ride
    #permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    #Only driver and passengers able to see rides
    queryset = Ride.objects.all()
    serializer_class = RideSerializer


class PrivateRideDetail(generics.RetrieveUpdateDestroyAPIView):
    ''''''
    queryset = PrivateRide.objects.all()
    serializer_class = PrivateRideSerializer


class DriverOnlyRide():
    pass

#TODO: add End ride endpoint.?