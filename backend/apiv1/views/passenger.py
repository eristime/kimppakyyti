from rest_framework import permissions, generics

from apiv1.serializers import PassengerSerializer
from apiv1.permissions import IsOwnerOrReadOnly, IsRideDriver, IsDriverOrPassengerReadOnly
from apiv1.models import Passenger


class PassengerList(generics.ListCreateAPIView):
    '''Passengers and drivers able to read. Only drivers able to add.'''
    #only drivers who have cars able to create a ride
    permission_classes = (IsDriverOrPassengerReadOnly,)
    serializer_class = PassengerSerializer

    def get_queryset(self):
        """
        This view should return all passengers on a ride.
        """
        ride = self.kwargs['pk']
        
        return Passenger.objects.filter(ride=ride)


class PassengerDetail(generics.RetrieveUpdateDestroyAPIView):
    '''Only driver able to modify.'''
    permission_classes = (IsRideDriver,)
    queryset = Passenger.objects.all()
    serializer_class = PassengerSerializer
