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


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer



class ProfileList(generics.ListCreateAPIView):
    #permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ProfileDetail(generics.RetrieveUpdateAPIView):
    #permission_classes = (permissions.IsAuthenticatedOrReadOnly)
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class CarDetail(generics.RetrieveUpdateDestroyAPIView):
    #permission_classes = (permissions.IsAuthenticatedOrReadOnly)
    queryset = Car.objects.all()
    serializer_class = CarSerializer

class CarList(generics.ListCreateAPIView):
    #permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Car.objects.all()
    serializer_class = CarSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)



class RideDetail(generics.RetrieveUpdateDestroyAPIView):
    #permission_classes = (permissions.IsAuthenticatedOrReadOnly)
    queryset = Ride.objects.all()
    serializer_class = RideSerializer

class RideList(generics.ListCreateAPIView):
    #permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
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

    def perform_create(self, serializer):
        serializer.save(timestamp=datetime.datetime.now())




@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        #TODO fill the rest
    })