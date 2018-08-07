import datetime


from django.contrib.auth.models import User

from rest_framework import mixins
from rest_framework import generics
from rest_framework import permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import renderers

from apiv1.models import Profile, Car, Ride, Message
from apiv1.serializers import UserSerializer, ProfileSerializer, CarSerializer, RideSerializer, MessageSerializer

#TODO: only admin able to see user list
class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

#TODO: only user able to see it's user list
class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer



class ProfileList(generics.ListCreateAPIView):
    # All able to see Profile
    #permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ProfileDetail(generics.RetrieveUpdateAPIView):
    #Only user able to modify profile
    #permission_classes = (permissions.IsAuthenticatedOrReadOnly)
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class CarDetail(generics.RetrieveUpdateDestroyAPIView):
    # Only user able to modify and see her cars
    #permission_classes = (permissions.IsAuthenticatedOrReadOnly)
    queryset = Car.objects.all()
    serializer_class = CarSerializer

class CarList(generics.ListCreateAPIView):
    # Only user able to modify and see her cars
    #permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Car.objects.all()
    serializer_class = CarSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)



class RideDetail(generics.RetrieveUpdateDestroyAPIView):
    #permission_classes = (permissions.IsAuthenticatedOrReadOnly)
    #Only driver and passengers able to see rides
    queryset = Ride.objects.all()
    serializer_class = RideSerializer

class RideList(generics.ListCreateAPIView):
    #permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    #Only driver and passengers able to see rides
    queryset = Ride.objects.all()
    serializer_class = RideSerializer



class MessageDetail(generics.RetrieveUpdateDestroyAPIView):
    #permission_classes = (permissions.IsAuthenticatedOrReadOnly)
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


class MessageList(generics.ListCreateAPIView):
    #permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Message.objects.all()
    serializer_class = MessageSerializer





@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        #TODO fill the rest
    })