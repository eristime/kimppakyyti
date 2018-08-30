from django.core.exceptions import PermissionDenied

from rest_framework import permissions
from rest_framework import generics
from rest_framework.serializers import ValidationError

from apiv1.serializers import EndRideSerializer, PassengerSerializer, AcceptRequestSerializer
from apiv1.permissions import IsDriver, IsRideDriver
from apiv1.models import Ride, Request, Passenger


class AcceptRequest(generics.CreateAPIView):
    '''Only meant for deving purposes'''
    permission_classes = (permissions.IsAuthenticated, IsRideDriver,)
    serializer_class = AcceptRequestSerializer
    queryset = Passenger.objects.all()


    def perform_create(self, serializer):
        '''
        Accepts a request for the ride.
        '''

        ride_pk = self.kwargs['pk']
        request_pk = self.kwargs['request_pk']
        ride_request = Request.objects.get(pk=request_pk)
        ride = Ride.objects.get(pk=ride_pk)

        # check that the user is the ride driver
        if self.request.user != ride.driver:
            raise PermissionDenied('Only driver can accept requests')

        # check that not passenger already
        for passenger in Passenger.objects.filter(ride=ride_pk):
            if self.request.user == passenger:
                raise ValidationError('Requester is already a passenger on the ride.')

        # check that room for passengers
        if ride.available_seats <= 0:
            raise ValidationError('Ride is already full.')

        # create new passenger based on the request
        serializer.save(ride=ride, user=ride_request.requester)

        # decrement available seats by one
        ride.available_seats = ride.available_seats - 1
        ride.save()

        # finally delete the request
        ride_request.delete()