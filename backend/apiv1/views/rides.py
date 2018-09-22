from rest_framework import permissions
from rest_framework import generics
from rest_framework import mixins
from rest_framework import viewsets
import django_filters.rest_framework as filters
from rest_framework.filters import OrderingFilter
#import rest_framework_filters as filters

from apiv1.serializers import RideSerializer, RideListSerializer, PrivateRideSerializer, StaffOnlyRideSerializer, DriverOnlyRideSerializer
from apiv1.permissions import IsOwnerOrReadOnly, IsDriver, IsDriverOrPassengerReadOnly
from apiv1.models import Ride, PrivateRide, DriverOnlyRide, StaffOnlyRide


class RideFilter(filters.FilterSet):
    
    time__gte = filters.TimeFilter(field_name='time', lookup_expr='gte',)

    class Meta:
        model = Ride
        fields = ('destination', 'departure', 'date', 'time__gte', )

class RideViewSet(viewsets.ModelViewSet):
    '''
    All able to see. Drivers with cars able to post. 
    '''
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
    queryset = Ride.objects.all()
    serializer_class = RideListSerializer
    filter_backends = (filters.DjangoFilterBackend, OrderingFilter,)
    filter_class = RideFilter
    #filter_fields = ('destination', 'departure', 'date',)
    
    #search_fields = ('destination', 'departure')
    #lookup_field = 'ride_pk'
    ordering = ('date', 'time',)

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
        
        return Ride.objects.filter(status=Ride.ONGOING)

    

  
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
