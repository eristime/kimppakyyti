from rest_framework import serializers
from apiv1.models import Request, Passenger


class RequestSerializer(serializers.ModelSerializer):
    ride = serializers.PrimaryKeyRelatedField(many=False, read_only=True,)
    requester = serializers.PrimaryKeyRelatedField(many=False, read_only=True,)
    status = serializers.ReadOnlyField()

    class Meta:
        model = Request
        fields = ('id', 'ride', 'requester', 'note', 'status', )


class RequestDetailSerializer(serializers.ModelSerializer):
    ride = serializers.PrimaryKeyRelatedField(many=False, read_only=True,)
    requester = serializers.PrimaryKeyRelatedField(many=False, read_only=True,)
    #request_pk = serializers.IntegerField(source='id')
    
    class Meta:
        model = Request
        fields = ('id', 'ride', 'requester', 'note', 'status', )
        read_only_fields = ('id', 'ride', 'requester', 'status',)


class AcceptRequestSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(many=False, read_only=True, )
    ride = serializers.PrimaryKeyRelatedField(many=False, read_only=True, )
    
    class Meta:
        model = Passenger
        fields = ('id', 'user', 'ride')
