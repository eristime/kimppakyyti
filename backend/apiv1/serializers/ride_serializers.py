from datetime import date
from django.contrib.auth.models import User
from rest_framework import serializers
from apiv1.models import Ride, PrivateRide, StaffOnlyRide, DriverOnlyRide
from .fields import UserCarField
from .profile_serializers import UserProfileSerializer
from .car_serializers import CarSerializer


class RideSerializer(serializers.ModelSerializer):
    private = serializers.PrimaryKeyRelatedField(many=False, read_only=True,)
    driver_only = serializers.PrimaryKeyRelatedField(many=False, read_only=True,)
    driver = serializers.PrimaryKeyRelatedField(many=False, read_only=True,)
    car = UserCarField(many=False)
 

    def validate_date(self, value):
        '''
        Check that date is not in the past.
        '''
        if value < date.today():
            raise serializers.ValidationError('Date cannot be set in the past.')

        return value


    def validate_car(self, value):
        '''
        Check that user is the car owner.
        '''

        if self.context['request'].user != value.owner:
            raise serializers.ValidationError('Driver needs to be the car owner.')

        return value
    

    class Meta:
        model = Ride
        fields = ('id', 'driver', 'car', 'destination', 'departure', 'date', 'time', 'available_seats','total_seat_count', 'estimated_fuel_cost', 'private', 'driver_only', )
        read_only_fields = ('total_seat_count', )


class RideListSerializer(serializers.ModelSerializer):
    private = serializers.PrimaryKeyRelatedField(many=False, read_only=True,)
    driver_only = serializers.PrimaryKeyRelatedField(many=False, read_only=True,)
    driver = UserProfileSerializer()
    car = CarSerializer()
    
    class Meta:
        model = Ride
        fields = ('id', 'driver', 'car', 'destination', 'departure', 'date', 'time', 'available_seats', 'total_seat_count', 'estimated_fuel_cost', 'private', 'driver_only', )


class EndRideSerializer(serializers.ModelSerializer):
    private = serializers.PrimaryKeyRelatedField(many=False, read_only=True,)
    driver_only = serializers.PrimaryKeyRelatedField(many=False, read_only=True,)
    driver = serializers.PrimaryKeyRelatedField(many=False, read_only=True,)
    
    class Meta:
        model = Ride
        fields = ('id', 'driver', 'car', 'destination', 'departure', 'date', 'time', 'available_seats', 'total_seat_count', 'estimated_fuel_cost', 'private', 'driver_only', )
        read_only_fields = ('id', 'driver', 'car', 'destination', 'departure', 'date', 'time', 'available_seats', 'total_seat_count', 'estimated_fuel_cost', 'private', 'driver_only', )


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
