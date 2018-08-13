from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the owner of the snippet.

        return obj.owner == request.user


class IsOwnerOrStaffReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it but staff to see it.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            if request.user.is_staff or obj.owner == request.user:
                return True

        # Write permissions are only allowed to the owner of the snippet.

        return obj.owner == request.user


class IsOwner(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to interact with it.
    """

    def has_object_permission(self, request, view, obj):

        # Write permissions are only allowed to the owner of the snippet.
        return obj.owner == request.user

#class IsDriverOrPassenger(permissions.BasePermission):
#    """
#    Custom permission to only allow owners of an object to edit it.
#    """
#
#    def has_object_permission(self, request, view, obj):
#        # Read permissions are allowed to any request,
#        # so we'll always allow GET, HEAD or OPTIONS requests.
#        if request.method in permissions.Da:
#            return True
#
#        # Write permissions are only allowed to the owner of the ride.
#        return obj.driver == request.user