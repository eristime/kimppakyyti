from rest_framework import permissions, generics

from apiv1.serializers import RequestSerializer, RequestDetailSerializer
from apiv1.permissions import IsRideDriver, IsRidePassengerOrDriverReadOnly, IsRequester, RideDriverReadOrAuthenticatedWrite, RideDriverRead
from apiv1.models import Request, Ride


class RequestList(generics.ListCreateAPIView):
    '''
    Drivers able to read. Users able to add themselves.
    IF POST: is authenticated
    If get: isDriver
    '''
    #only drivers who 
    permission_classes = (permissions.IsAuthenticated, RideDriverRead)
    serializer_class = RequestSerializer


    def perform_create(self, serializer):
        serializer.save(requester=self.request.user, ride=Ride.objects.get(pk=self.kwargs['pk']))


    def get_queryset(self):
        '''
        This view should return all request for a specific ride.
        '''
        
        ride = self.kwargs['pk']
        return Request.objects.filter(ride=ride, status='PENDING')


class RequestDetail(generics.RetrieveUpdateDestroyAPIView):
    '''
    Only request owner able to remove the request.
    '''
    permission_classes = (IsRequester,)
    queryset = Request.objects.all()
    serializer_class = RequestDetailSerializer
    #lookup_field = 'request_pk'

    #def get_queryset(self):
    #    '''
    #    Only return requests that are not accepted.
    #    '''
    #    ride = self.kwargs['pk']
    #    return Request.objects.filter(ride=ride, status='PENDING')
