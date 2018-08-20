from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework import generics

from apiv1.models import Request
from apiv1.serializers import RequestSerializer


class UserRequests(generics.ListAPIView):
    ''' Only logged in user able to see her requests'''
    permission_classes = (permissions.IsAuthenticated, )
    serializer_class = RequestSerializer


    def get_queryset(self):
        """
        This should return all requests made by user.
        """

        if self.request.user.is_anonymous:
            return Request.objects.none()

        return Request.objects.filter(requester=self.request.user)
    