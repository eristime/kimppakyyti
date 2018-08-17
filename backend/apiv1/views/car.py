from django.contrib.auth.models import User
from rest_framework import permissions, generics

from apiv1.models import Car
from apiv1.serializers import CarSerializer
from apiv1.permissions import IsOwner, IsOwnerOrWriteOnly, IsOwnerOrReadOnly



class CarDetail(generics.RetrieveUpdateDestroyAPIView):
    '''Only user able to modify and see her cars. Cars able to be deleted.''' 
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class CarList(generics.ListCreateAPIView):
    ''' Only user able to modify and see her cars'''
    permission_classes = (permissions.IsAuthenticated, )
    serializer_class = CarSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        """
        This view should return all passengers on a ride.
        """
        ##TODO handle anonymous users
        if self.request.user.is_anonymous:
            return Car.objects.none()

        return Car.objects.filter(owner=self.request.user)
    