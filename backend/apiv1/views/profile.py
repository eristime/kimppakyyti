from django.contrib.auth.models import User
from rest_framework import permissions, generics

from apiv1.serializers import StaffProfileSerializer, PrivateProfileSerializer, ProfileSerializer
from apiv1.permissions import IsOwner, IsOwnerOrReadOnly, IsOwnerOrStaffReadOnly
from apiv1.models.profiles import *


class ProfileDetail(generics.RetrieveUpdateAPIView):
    '''Only user able to modify profile. All able to see it'''
    #TODO add owner property to profile model so that authentication works (owner vs user?)
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class PrivateProfileDetail(generics.RetrieveUpdateAPIView):
    '''Only user and staff able to interact with profile'''
    #TODO add owner property to profile model so that authentication works (owner vs user?)
    permission_classes = (IsOwnerOrStaffReadOnly,)
    queryset = PrivateProfile.objects.all()
    serializer_class = PrivateProfileSerializer


class StaffProfileDetail(generics.RetrieveUpdateAPIView):
    '''Used to save data for staff use.'''
    permission_classes = (permissions.IsAdminUser,)
    #TODO add owner property to profile model so that authentication works (owner vs user?)
    queryset = StaffProfile.objects.all()
    serializer_class = StaffProfileSerializer