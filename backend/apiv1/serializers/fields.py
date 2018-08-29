from rest_framework import serializers
from apiv1.models import Car


class UserCarField(serializers.PrimaryKeyRelatedField):
    '''
    Field which returns only user cars.
    '''
    def get_queryset(self):
        user = self.context['request'].user
        queryset = Car.objects.filter(owner=user)
        return queryset
