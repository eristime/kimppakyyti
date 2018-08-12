

#
#from django.contrib.auth.models import User
#
#from rest_framework import mixins
#from rest_framework import generics
#from rest_framework import permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
#from rest_framework import renderers
#
#from apiv1.models import Profile, Car, Ride, Message
#from apiv1.serializers import UserSerializer, ProfileSerializer, CarSerializer, RideSerializer #MessageSerializer
#
#from apiv1.permissions import IsOwner, IsOwnerOrReadOnly
#
#
##TODO: only admin able to see user list
#class UserList(generics.ListAPIView):
#    queryset = User.objects.all()
#    serializer_class = UserSerializer
#
#
##TODO: only user able to see it's user details (or not)?
#class UserDetail(generics.RetrieveAPIView):
#    queryset = User.objects.all()
#    serializer_class = UserSerializer
#
#    def get_queryset():
#        return User.objects.all().filter(username=self.request.user)
#
#
#
#class ProfileList(generics.ListCreateAPIView):
#    # All able to see Profile
#    #permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
#    queryset = Profile.objects.all()
#    serializer_class = ProfileSerializer
#
#    def perform_create(self, serializer):
#        serializer.save(user=self.request.user)
#
#
#class ProfileDetail(generics.RetrieveUpdateAPIView):
#    '''Only user able to modify profile. All able to see it'''
#    permission_classes = (IsOwnerOrReadOnly,)
#    queryset = Profile.objects.all()
#    serializer_class = ProfileSerializer
#
#
#class CarDetail(generics.RetrieveUpdateDestroyAPIView):
#    '''Only user able to modify and see her cars. Cars able to be deleted.''' 
#    permission_classes = (isOwner,)
#    queryset = Car.objects.all()
#    serializer_class = CarSerializer
#
#
#
#class CarList(generics.ListCreateAPIView):
#    ''' Only user able to modify and see her cars'''
#    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
#    queryset = Car.objects.all()
#    serializer_class = CarSerializer
#
#    def perform_create(self, serializer):
#        serializer.save(owner=self.request.user)
#    
#
#    #def get_queryset(self):
#    #   return Car.objects.all().filter(owner=self.request.user)
#    
#class RideDetail(generics.RetrieveUpdateDestroyAPIView):
#    '''All able to see. Only driver able to modify.'''
#    permission_classes = (permissions.IsOwnerOrReadOnly)
#    serializer_class = RideSerializer
#
#    #def get_queryset(self):
#    #    return Ride.objects.all().filter(user=self.request.user)
#
#
#class RideList(generics.ListCreateAPIView):
#    '''All able to see. Drivers with cars able to post. (done automatically?)'''
#    #only drivers who have cars able to create a ride
#    #permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
#    #Only driver and passengers able to see rides
#    queryset = Ride.objects.all()
#    serializer_class = RideSerializer
#
#
## 
#
##
##class MessageDetail(generics.RetrieveUpdateDestroyAPIView):
##    #permission_classes = (permissions.IsAuthenticatedOrReadOnly)
##    queryset = Message.objects.all()
##    serializer_class = MessageSerializer
##
##
##class MessageList(generics.ListCreateAPIView):
##    #permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
##    queryset = Message.objects.all()
##    serializer_class = MessageSerializer
##
#
#
#

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        #TODO fill the rest
    })