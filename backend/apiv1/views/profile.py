from django.contrib.auth.models import User
from rest_framework import permissions, generics

from apiv1.serializers import ProfileSerializer
from apiv1.permissions import IsOwner, IsOwnerOrReadOnly
from apiv1.models import Profile

class ProfileList(generics.ListCreateAPIView):
    # All able to see Profile
    #permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    def perform_create(self, serializer):
        #TODO if profile exists, return
        serializer.save(user=self.request.user)


class ProfileDetail(generics.RetrieveUpdateAPIView):
    '''Only user able to modify profile. All able to see it'''
    #permission_classes = (IsOwnerOrReadOnly,)
    #TODO add owner property to profile model so that authentication works (owner vs user?)
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

  #TODO: add view for PrivateProfile