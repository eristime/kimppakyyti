from rest_framework import permissions
from apiv1.models.rides import PrivateRide


class IsOwnerOrReadOnly(permissions.BasePermission):
    '''
    Custom permission to only allow owners of an object to edit it.
    '''

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the owner of the snippet.

        return obj.owner == request.user

class IsOwnerOrWriteOnly(permissions.BasePermission):
    '''
    Custom permission to only allow owners of an object to edit it.
    '''

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return obj.owner == request.user

        # Write permissions are only allowed to the owner of the snippet.

        return True


class IsOwnerOrStaffReadOnly(permissions.BasePermission):
    '''
    Custom permission to only allow owners of an object to edit it but staff to see it.
    '''

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            if request.user.is_staff or obj.owner == request.user:
                return True

        # Write permissions are only allowed to the owner of the snippet.

        return obj.owner == request.user


class IsOwner(permissions.BasePermission):
    '''
    Custom permission to only allow owners of an object to interact with it.
    '''

    def has_object_permission(self, request, view, obj):

        # Write permissions are only allowed to the owner of the snippet.
        return obj.owner == request.user


class IsRequester(permissions.BasePermission):
    '''
    Custom permission to only allow requesters of an object to interact with it.
    '''

    def has_object_permission(self, request, view, obj):

        return obj.requester == request.user


class IsDriver(permissions.BasePermission):
    '''
    Custom permission to only allow drivers of a ride to interact with it.
    '''

    def has_object_permission(self, request, view, obj):

        # Write permissions are only allowed to the owner of the snippet.
        return obj.driver == request.user


class IsRideDriver(permissions.BasePermission):
    '''
    For object with ride-field.Custom permission to only allow drivers of a ride to interact with it.
    '''

    def has_object_permission(self, request, view, obj):

        return obj.ride.driver == request.user



class IsDriverOrPassengerReadOnly(permissions.BasePermission):
    '''
    Custom permission to only allow driver to modify and passenger to see.
    '''

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        
        if request.method in permissions.SAFE_METHODS:
            
            #TODO check that this works
            #ride_pk = pk
            #passengers = PrivateRide.objects.filter(pk=ride_pk).passengers
            print('custom_permission: passengers', view.kwargs['passengers'])

            return True #|| passengers.filter(request.user).exists()

        # Write permissions are only allowed to the owner of the ride.
        return obj.driver == request.user


class IsRidePassengerOrDriverReadOnly(permissions.BasePermission):
    '''
    For objects with ride field. Custom permission to only allow passengers to modify and drivers to see.
    '''

    def has_object_permission(self, request, view, obj):

        if request.method in permissions.SAFE_METHODS:
            
            return obj.ride.driver == request.user 

        return obj.ride.passengers.get(request.user.pk).exists()


class IsRideDriverOrDriverReadOnly(permissions.BasePermission):
    '''
    For objects with ride field. Custom permission to only allow passengers to modify and drivers to see.
    '''

    def has_object_permission(self, request, view, obj):

        if request.method in permissions.SAFE_METHODS:
            
            return obj.ride.driver == request.user 

        return obj.ride.passengers.get(request.user.pk).exists()


class IsAuthenticatedOrDriverReadOnly(permissions.BasePermission):
    '''
    Drivers not able to post, only read.
    '''

    def has_object_permission(self, request, view, obj):

        if request.method in permissions.SAFE_METHODS:
            
            return obj.ride.driver == request.user 

        return obj.ride.passengers.get(request.user.pk).exists()


class RideDriverReadOrAuthenticatedWrite(permissions.BasePermission):
    '''
    Read access: RideDriver
    Others: authenticated
    '''

    def has_object_permission(self, request, view, obj):
        
        return False and obj.ride.driver != request.user 

        if request.method in permissions.SAFE_METHODS:
            
            #Ride.objects.get(pk=self.kwargs['pk'])
            print(obj)
            obj.something

            return False and obj.ride.driver != request.user 

        return request.user.is_authenticated

class RideDriverRead(permissions.BasePermission):
    '''
    Read access: RideDriver
    Others: authenticated
    '''

    def has_object_permission(self, request, view, obj):
        
        safe_methods = permissions.SAFE_METHODS

        if True:
            return False
        if request.method in permissions.SAFE_METHODS:

            return False

            #return obj.ride.driver == request.user 
