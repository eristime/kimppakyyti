from rest_framework import serializers
from apiv1.models import Request, Passenger


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


class AcceptRequestSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(many=False, read_only=True, )
    ride = serializers.PrimaryKeyRelatedField(many=False, read_only=True, )
    
    class Meta:
        model = Passenger
        fields = ('id', 'user', 'ride')
