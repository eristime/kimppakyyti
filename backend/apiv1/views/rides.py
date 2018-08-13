from rest_framework import permissions, generics

from apiv1.serializers import RideSerializer, PrivateRideSerializer, StaffOnlyRideSerializer, DriverOnlyRideSerializer
from apiv1.permissions import IsOwnerOrReadOnly, IsDriver, IsDriverOrPassengerReadOnly
from apiv1.models import Ride, PrivateRide, DriverOnlyRide, StaffOnlyRide


class RideList(generics.ListCreateAPIView):
    '''All able to see. Drivers with cars able to post. (done automatically?)'''
    #only drivers who have cars able to create a ride
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    #Only driver and passengers able to see rides
    queryset = Ride.objects.all()
    serializer_class = RideSerializer


class RideDetail(generics.RetrieveUpdateDestroyAPIView):
    '''Only driver able to modify.'''
    permission_classes = (IsDriver,)
    queryset = Ride.objects.all()
    serializer_class = RideSerializer


class PrivateRideDetail(generics.RetrieveUpdateAPIView):
    '''Passengers can view, drivers can modify.'''
    #permission_classes = (IsDriverOrPassengerReadOnly, )
    queryset = PrivateRide.objects.all()
    serializer_class = PrivateRideSerializer
    
    #TODO add custom method for put
    #item = self.kwargs['pk']


class StaffOnlyRideDetail(generics.RetrieveUpdateAPIView):
    '''Only driver able to modify.'''
    permission_classes = (permissions.IsAdminUser, )
    queryset = StaffOnlyRide.objects.all()
    serializer_class = StaffOnlyRideSerializer


class DriverOnlyRideDetail(generics.RetrieveUpdateAPIView):
    '''Only driver able to modify.'''
    #permission_classes = (IsDriver,) #TODO how to check if driver
    queryset = DriverOnlyRide.objects.all()
    serializer_class = DriverOnlyRideSerializer


#TODO: add End ride endpoint.?