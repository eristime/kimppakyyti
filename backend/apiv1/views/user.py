from django.contrib.auth.models import User
from rest_framework import permissions, generics

from apiv1.serializers import UserSerializer
from apiv1.permissions import IsOwner

#TODO: only admin able to see user list
class UserList(generics.ListAPIView):
    '''Post a new user. See all users.'''
    queryset = User.objects.all()
    serializer_class = UserSerializer


#TODO: only user able to see it's user details (or not)?
class UserDetail(generics.RetrieveAPIView):
    '''Edit users details if user.'''
    queryset = User.objects.all()
    serializer_class = UserSerializer

    #def get_queryset():
    #    return User.objects.all().filter(username=self.request.user)