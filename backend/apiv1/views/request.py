from rest_framework import permissions, generics

from apiv1.serializers import RequestSerializer, RequestUpdateSerializer
from apiv1.permissions import IsRideDriver, IsRidePassengerOrDriverReadOnly
from apiv1.models import Request, Ride


class RequestList(generics.ListCreateAPIView):
    '''Drivers able to read. Users able to add themselves.'''
    #only drivers who have cars able to create a ride
    #permission_classes = (IsAuthenticatedOrDriverReadOnly,)
    #queryset = Request.objects.all()
    serializer_class = RequestSerializer

    def perform_create(self, serializer):
        serializer.save(requester=self.request.user, ride=Ride.objects.get(pk=self.kwargs['pk']), status='PENDING')
        #TODO: if request exists, not able to post another one
        #TODO: if driver, not able to post request
        #TODO: if passenger, not able to post request 

    def get_queryset(self):
        """
        This view should return all request for a specific ride.
        """
        
        ride = self.kwargs['pk']
        return Request.objects.filter(ride=ride, status='pending')


class RequestDetail(generics.RetrieveUpdateAPIView):
    #TODO make a custom request/:id/accept route
    '''Only driver able to modify.'''
    #permission_classes = (IsRideDriver,)
    queryset = Request.objects.all()
    serializer_class = RequestUpdateSerializer

    def get_queryset(self):
        """
        Only return requests that are not accepted.
        """
        ride = self.kwargs['pk']
        return Request.objects.filter(ride=ride, status='pending')
