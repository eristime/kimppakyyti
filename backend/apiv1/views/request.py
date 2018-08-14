from rest_framework import permissions, generics

from apiv1.serializers import RequestSerializer
from apiv1.permissions import IsRideDriver, IsRidePassengerOrDriverReadOnly
from apiv1.models import Request


class RequestList(generics.ListCreateAPIView):
    '''Drivers able to read. Users able to add themselves.'''
    #only drivers who have cars able to create a ride
    #permission_classes = (IsRidePassengerOrDriverReadOnly,)
    #queryset = Request.objects.all()
    serializer_class = RequestSerializer

    def perform_create(self, serializer):
        serializer.save(requester=self.request.user)
        print("self.kwargs['pk']", self.kwargs['pk'])
        serializer.save(ride=self.kwargs['pk'])

    def get_queryset(self):
        """
        This view should return all request for a specific ride.
        """
        ride = self.kwargs['pk']
        return Request.objects.filter(ride=ride)


class RequestDetail(generics.RetrieveUpdateDestroyAPIView):
    '''Only driver able to modify.'''
    permission_classes = (IsRideDriver,)
    queryset = Request.objects.all()
    serializer_class = RequestSerializer


    
    #def perform_update(self, serializer):
    #    serializer.save(requester=self.request.user)
