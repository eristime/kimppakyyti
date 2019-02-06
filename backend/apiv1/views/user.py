from django.contrib.auth.models import User
from rest_framework import permissions, generics

from apiv1.serializers import UserSerializer


class UserList(generics.ListAPIView):
    '''See all users.'''
    queryset = User.objects.all()
    permission_classes = (permissions.IsAdminUser,)
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    '''Edit users details if user.'''
    queryset = User.objects.all()
    permission_classes = (permissions.IsAdminUser,)
    serializer_class = UserSerializer

    #def get_queryset():
    #    return User.objects.all().filter(username=self.request.user)