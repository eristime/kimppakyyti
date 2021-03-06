from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework import generics

from apiv1.models import Car
from apiv1.serializers import CarSerializer
from apiv1.permissions import IsOwnerOrReadOnly, IsOwner


class CarDetail(generics.RetrieveDestroyAPIView):
    '''Only user able to modify and see her cars. Cars able to be deleted.''' 
    permission_classes = (IsOwner,)
    queryset = Car.objects.all()
    serializer_class = CarSerializer

    #TODO: override deletion, can't delete if used in ongoing ride


class CarList(generics.ListCreateAPIView):
    ''' Only user able to modify and see her cars'''
    permission_classes = (permissions.IsAuthenticated, )
    serializer_class = CarSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        """
        This view should return only current user cars.
        """

        if self.request.user.is_anonymous:
            return Car.objects.none()

        return Car.objects.filter(owner=self.request.user)
    