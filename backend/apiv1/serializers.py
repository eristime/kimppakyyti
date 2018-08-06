from rest_framework import serializers
from apiv1.models import Profile, Car, Ride, Message
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    rides = serializers.PrimaryKeyRelatedField(many=True, queryset=Ride.objects.all())
    cars = serializers.PrimaryKeyRelatedField(many=True, queryset=Car.objects.all())
    sent_messages = serializers.PrimaryKeyRelatedField(many=True, queryset=Message.objects.all())
    received_messages = serializers.PrimaryKeyRelatedField(many=True, queryset=Message.objects.all())
    #profile = serializers.PrimaryKeyRelatedField(many=True, queryset=Profile.objects.all()) # TODO: add profile information

    class Meta:
        model = User
        fields = ('id', 'username', 'rides', 'cars', 'sent_messages', 'received_messages')


class ProfileSerializer(serializers.ModelSerializer):
    
    user = serializers.ReadOnlyField(source='owner.username')
    
    class Meta:
        model = Profile
        fields = ('id', 'user', 'first_name', 'last_name', 'phone_number', 'photo', )



class CarSerializer(serializers.ModelSerializer):

    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Car
        fields = ('id', 'owner', 'model', 'register_plate', 'consumption')



class RideSerializer(serializers.ModelSerializer):
    messages = serializers.PrimaryKeyRelatedField(many=True, queryset=Message.objects.all())
    driver = serializers.ReadOnlyField(source='owner.username')

    
    class Meta:
        model = Ride
        fields = ('id', 'driver', 'messages', 'destination', 'departure', 'available_seats', 'status', 'car', 'estimated_fuel_cost', 'recurrent')


class MessageSerializer(serializers.ModelSerializer):
    #owner = serializers.ReadOnlyField(source='owner.username')
    
    class Meta:
        model = Message
        fields = ('id', 'ride', 'sender', 'receiver', 'body', 'timestamp', 'inappropriate')