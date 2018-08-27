

#
#from django.contrib.auth.models import User
#
#from rest_framework import mixins
#from rest_framework import generics
#from rest_framework import permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
#from rest_framework import renderers


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        #'profiles': reverse('profile-list', request=request, format=format),
        'rides': reverse('ride-list', request=request, format=format),
        #'end-ride': reverse('end-ride', request=request, format=format),
        'my rides as driver': reverse('user-rides-as-driver-list', request=request, format=format),
        'my rides as passenger': reverse('user-rides-as-passenger-list', request=request, format=format),
        'my ride requests': reverse('user-request-list', request=request, format=format),
        'my cars': reverse('car-list', request=request, format=format),
        #TODO name url names consistently
    })