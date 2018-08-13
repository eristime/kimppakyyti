from rest_framework import serializers
from apiv1.models import Profile, StaffProfile, Car, Ride, PrivateRide, DriverOnlyRide, Message
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    #rides = serializers.PrimaryKeyRelatedField(many=True, queryset=Ride.objects.all())
    #cars = serializers.PrimaryKeyRelatedField(many=True, queryset=Car.objects.all())
    #sent_messages = serializers.PrimaryKeyRelatedField(many=True, queryset=Message.objects.all())
    #received_messages = serializers.PrimaryKeyRelatedField(many=True, queryset=Message.objects.all())
    profile = serializers.PrimaryKeyRelatedField(many=False, read_only=True,)

    class Meta:
        model = User
        fields = ('id', 'username', 'profile',)


class ProfileSerializer(serializers.ModelSerializer):
    
    #user = serializers.ReadOnlyField(source='owner.username')
    
    class Meta:
        model = Profile
        fields = ('id', 'first_name', 'last_name', 'phone_number', 'photo')


class PrivateProfileSerializer(serializers.ModelSerializer):
    
    #user = serializers.ReadOnlyField(source='owner.username')
    
    class Meta:
        model = Profile
        fields = ('id', 'phone_number', )



class StaffProfileSerializer(serializers.ModelSerializer):
    
    #user = serializers.ReadOnlyField(source='owner.username')
    
    class Meta:
        model = StaffProfile
        fields = ('id', 'reported_count', 'deleted', 'is_active',)



class CarSerializer(serializers.ModelSerializer):

    owner = serializers.ReadOnlyField(source='owner.username')
    #owner = serializers.PrimaryKeyRelatedField(many=False, read_only=True,)

    class Meta:
        model = Car
        fields = ('id', 'owner', 'model', 'register_plate', 'consumption')



class RideSerializer(serializers.ModelSerializer):
    #messages = serializers.PrimaryKeyRelatedField(many=True, queryset=Message.objects.all())
    #driver = serializers.ReadOnlyField(source='owner.username')
    

    
    class Meta:
        model = Ride
        fields = ('id', 'driver', 'car', 'destination', 'departure', 'available_seats', 'status', 'estimated_fuel_cost', 'private', 'driver_only', )


class PrivateRideSerializer(serializers.ModelSerializer):
    #messages = serializers.PrimaryKeyRelatedField(many=True, queryset=Message.objects.all())
    #driver = serializers.ReadOnlyField(source='owner.username')
    #ride = serializers.PrimaryKeyRelatedField(many=False, read_only=True,)
    
    class Meta:
        model = Ride
        fields = ('__all__')



#class MessageSerializer(serializers.ModelSerializer):
#    #owner = serializers.ReadOnlyField(source='owner.username')
#    
#    class Meta:
#        model = Message
#        fields = ('id', 'ride', 'sender', 'receiver', 'body')