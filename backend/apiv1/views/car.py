from django.contrib.auth.models import User
from rest_framework import permissions, generics

from apiv1.models import Car
from apiv1.serializers import CarSerializer
from apiv1.permissions import IsOwner



class CarDetail(generics.RetrieveUpdateDestroyAPIView):
    '''Only user able to modify and see her cars. Cars able to be deleted.''' 
    permission_classes = (IsOwner,)
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class CarList(generics.ListCreateAPIView):
    ''' Only user able to modify and see her cars'''
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Car.objects.all()
    serializer_class = CarSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    

    #def get_queryset(self):
    #   return Car.objects.all().filter(owner=self.request.user)