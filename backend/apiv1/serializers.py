from rest_framework import serializers
from apiv1.models import *
from django.contrib.auth.models import User
from datetime import datetime


class UserSerializer(serializers.ModelSerializer):
    #rides_as_driver = serializers.PrimaryKeyRelatedField(many=True, queryset=Ride.objects.all(), source='driver')
    #rides_as_passenger
    cars = serializers.PrimaryKeyRelatedField(many=True, queryset=Car.objects.all())
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


class UserProfileSerializer(serializers.ModelSerializer):
    
    profile = ProfileSerializer()

    class Meta:
        model = User
        fields = ('id', 'profile',)


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
    private = serializers.PrimaryKeyRelatedField(many=False, read_only=True,)
    driver_only = serializers.PrimaryKeyRelatedField(many=False, read_only=True,)
    driver = serializers.PrimaryKeyRelatedField(many=False, read_only=True,)

    def validate_date(self, value):
        '''
        Check that date is not in the past.
        '''
        if datetime.now() < value:
            raise serializers.ValidationError('Date cannot be set in the past.')

        return value
    
    class Meta:
        model = Ride
        fields = ('id', 'driver', 'car', 'destination', 'departure', 'date', 'available_seats','total_seat_count', 'estimated_fuel_cost', 'private', 'driver_only', )


class RideProfileCombinedSerializer(serializers.ModelSerializer):
    private = serializers.PrimaryKeyRelatedField(many=False, read_only=True,)
    driver_only = serializers.PrimaryKeyRelatedField(many=False, read_only=True,)
    driver = UserProfileSerializer()
    
    class Meta:
        model = Ride
        fields = ('id', 'driver', 'car', 'destination', 'departure', 'date', 'available_seats', 'total_seat_count', 'estimated_fuel_cost', 'private', 'driver_only', )


class EndRideSerializer(serializers.ModelSerializer):
    private = serializers.PrimaryKeyRelatedField(many=False, read_only=True,)
    driver_only = serializers.PrimaryKeyRelatedField(many=False, read_only=True,)
    driver = serializers.PrimaryKeyRelatedField(many=False, read_only=True,)
    
    class Meta:
        model = Ride
        fields = ('id', 'driver', 'car', 'destination', 'departure', 'date', 'available_seats', 'total_seat_count', 'estimated_fuel_cost', 'private', 'driver_only', )
        read_only_fields = ('id', 'driver', 'car', 'destination', 'departure', 'date', 'available_seats', 'total_seat_count', 'estimated_fuel_cost', 'private', 'driver_only', )



class PrivateRideSerializer(serializers.ModelSerializer):
    
    ride = serializers.ReadOnlyField(source='ride.id')

    class Meta:
        model = PrivateRide
        fields = ('ride', 'passengers')


class DriverOnlyRideSerializer(serializers.ModelSerializer):
    
    ride = serializers.ReadOnlyField(source='ride.id')

    class Meta:
        model = DriverOnlyRide
        fields = ('ride', )


class StaffOnlyRideSerializer(serializers.ModelSerializer):
    
    ride = serializers.ReadOnlyField(source='ride.id')

    class Meta:
        model = StaffOnlyRide
        fields = ('ride', )


class RequestSerializer(serializers.ModelSerializer):
    ride = serializers.PrimaryKeyRelatedField(many=False, read_only=True,)
    requester = serializers.PrimaryKeyRelatedField(many=False, read_only=True,)
    status = serializers.ReadOnlyField()
    
    class Meta:
        model = Request
        fields = ('id', 'ride', 'requester', 'note', 'status', )


class RequestUpdateSerializer(serializers.ModelSerializer):
    ride = serializers.PrimaryKeyRelatedField(many=False, read_only=True,)
    requester = serializers.PrimaryKeyRelatedField(many=False, read_only=True,)
    note = serializers.ReadOnlyField()
    
    class Meta:
        model = Request
        fields = ('id', 'ride', 'requester', 'note', 'status', )


class PassengerSerializer(serializers.ModelSerializer):
    #user = serializers.PrimaryKeyRelatedField(many=False, )
    ride = serializers.PrimaryKeyRelatedField(many=False, read_only=True, )
    
    class Meta:
        model = Passenger
        fields = ('id', 'user', 'ride')


class AcceptRequestSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(many=False, read_only=True, )
    ride = serializers.PrimaryKeyRelatedField(many=False, read_only=True, )
    
    class Meta:
        model = Passenger
        fields = ('id', 'user', 'ride')


#class MessageSerializer(serializers.ModelSerializer):
#    #owner = serializers.ReadOnlyField(source='owner.username')
#    
#    class Meta:
#        model = Message
#        fields = ('id', 'ride', 'sender', 'receiver', 'body')