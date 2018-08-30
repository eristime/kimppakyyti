from rest_framework import permissions
from rest_framework import generics
from rest_framework import mixins
from rest_framework import viewsets
import django_filters.rest_framework

from apiv1.serializers import RideSerializer, RideListSerializer, PrivateRideSerializer, StaffOnlyRideSerializer, DriverOnlyRideSerializer
from apiv1.permissions import IsOwnerOrReadOnly, IsDriver, IsDriverOrPassengerReadOnly
from apiv1.models import Ride, PrivateRide, DriverOnlyRide, StaffOnlyRide


class RideViewSet(viewsets.ModelViewSet):
    '''
    All able to see. Drivers with cars able to post. (done automatically?)
    '''
    #only drivers who have cars able to create a ride
    permission_classes = (permissions.IsAuthenticated,)
    #Only driver and passengers able to see rides
    queryset = Ride.objects.all()
    serializer_class = RideListSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
    filter_fields = ('driver', 'car', 'destination', 'departure', 'date')
    ordering_fields = ('date', 'destination', 'departure')
    #search_fields = ('destination', 'departure')
    #lookup_field = 'ride_pk'

    def get_serializer_class(self):
        if self.action == 'list':
            return RideListSerializer
        if self.action == 'create':
            return RideSerializer


    def perform_create(self, serializer):
        serializer.save(driver=self.request.user)


    def get_queryset(self):
        '''
        This view should return all request for a specific ride.
        '''
        
        return Ride.objects.filter(status='ONGOING')

  
class RideDetail(generics.RetrieveAPIView):
    '''
    Ride details. Only read available. Available for authenticated users.
    '''
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Ride.objects.all()
    serializer_class = RideSerializer
    #lookup_field = 'id'
    #lookup_fields = ('ride_id', )
    #lookup_url_kwarg = 'ride_id'


class PrivateRideDetail(generics.RetrieveUpdateAPIView):
    '''
    Passengers can view, drivers can modify.
    '''
    #permission_classes = (IsDriverOrPassengerReadOnly, )
    queryset = PrivateRide.objects.all()
    serializer_class = PrivateRideSerializer
    #lookup_field = 'ride_pk'
    
    #TODO add custom method for put
    #item = self.kwargs['pk']


class StaffOnlyRideDetail(generics.RetrieveUpdateAPIView):
    '''
    Only driver able to modify.
    '''
    permission_classes = (permissions.IsAdminUser, )
    queryset = StaffOnlyRide.objects.all()
    serializer_class = StaffOnlyRideSerializer
    #lookup_field = 'ride_pk'


class DriverOnlyRideDetail(generics.RetrieveUpdateAPIView):
    '''
    Only driver able to modify.
    '''
    #permission_classes = (IsDriver,) #TODO how to check if driver
    queryset = DriverOnlyRide.objects.all()
    serializer_class = DriverOnlyRideSerializer
    #lookup_field = 'ride_pk'
