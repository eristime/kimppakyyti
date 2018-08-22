from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication
from rest_framework import permissions
from rest_framework import generics
from rest_framework.exceptions import APIException

from apiv1.serializers import EndRideSerializer, PassengerSerializer, AcceptRequestSerializer
from apiv1.permissions import IsDriver, IsRideDriver
from apiv1.models import Ride, Request, User, Passenger


class AcceptPassenger(APIView):
    '''Only driver able to modify.'''
    permission_classes = (IsDriver,) 
    queryset = Ride.objects.all()
    serializer_class = EndRideSerializer


    # check if eligble to accept for the ride
    # remove ride request
    #if succeeded add a passenger

    def post(self, request, format=None):
        
        """
        Accept a request for a ride. Removes the request and adds a passanger.
        """

        ride = Ride.objects.get(self.kwargs['pk'])
        request = Request.objects.get(self.kwargs['request_pk'])
        user = User.object.get(request.user)
        request.delete()


        return Request.objects.filter(ride=ride, status='pending')
        usernames = [user.username for user in User.objects.all()]
        return Response(usernames)


class AcceptRequest(generics.CreateAPIView):
    '''Only meant for deving purposes'''
    #only drivers who have cars able to create a ride
    #permission_classes = (IsRideDriver,)
    serializer_class = AcceptRequestSerializer
    queryset = Passenger.objects.all()


    def perform_create(self, serializer):
        """
        Accepts a request for the ride.
        """

        ride_pk = self.kwargs['pk']
        request_pk = self.kwargs['request_pk']
        #return Response('ride:%s request:%s' % (ride_pk, request_pk))

        request = Request.objects.get(pk=request_pk)
        ride = Ride.objects.get(pk=ride_pk)
        #requester = User.objects.get(pk=request.requester)

        requester = request.requester
        # check that not passenger already
        #if user in Passenger.objects.filter(ride=ride_pk).get(request.user):
        #    return Response('Requester is already a passenger on the ride.')


        # check that room for passengers
        #if ride.available_seats <= 0:
        #    return Response('Ride is already full.')


        serializer.save(ride=ride, user=request.requester)


        # decrement available seats by one
        #ride.available_seats = ride.available_seats - 1
        #ride.save()

        # finally delete the request
        request.delete()