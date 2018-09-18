from rest_framework import permissions, generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework.serializers import ValidationError
from rest_framework import viewsets

from apiv1.serializers import RequestListSerializer, RequestCreateSerializer, RequestDetailSerializer
from apiv1.permissions import IsRequester
from apiv1.models import Request, Ride, Passenger


class RequestViewSet(viewsets.ModelViewSet):
    '''
    Drivers able to see the ride requests. Authenticated users able to create requets for rides.
    '''
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = RequestListSerializer


    def get_serializer_class(self):
        if self.action == 'list':
            return RequestListSerializer
        if self.action == 'create':
            return RequestCreateSerializer


    def perform_create(self, serializer):

        ride = Ride.objects.get(pk=self.kwargs['pk'])

        if Request.objects.filter(requester=self.request.user, ride=ride).exists():
            raise ValidationError('User can have only one request per ride.')


        if ride.status !='ONGOING':
            raise ValidationError('Not possible to add requests to ride which are not ongoing.')

        if self.request.user == ride.driver:
            raise ValidationError('Driver can\'t make requests to her own ride.')


        for passenger in Passenger.objects.filter(ride=ride):
            if self.request.user == passenger.user:
                raise ValidationError('User can\'t make requests if already passenger.')


        serializer.save(requester=self.request.user, ride=ride)


    def get_queryset(self):
        '''
        This view should return all request for a specific ride if ride driver. Otherwise don't return anything.
        '''
        ride_pk = self.kwargs['pk']
        
        if self.request.user == Ride.objects.get(pk=ride_pk).driver:
            return Request.objects.filter(ride=ride_pk, status='PENDING')

        return Request.objects.none()


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
