from rest_framework import serializers
from apiv1.models import User, Car, Ride, Message


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('token', 'first_name', 'last_name')