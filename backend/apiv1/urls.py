from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from apiv1 import views


ride_list = views.RideViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

request_list = views.RequestViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

urlpatterns = format_suffix_patterns([
    url(r'^$', views.api_root),

    url(r'^users/$',
        views.UserList.as_view(),
        name='user-list'),

    url(r'^users/(?P<pk>[0-9]+)/$',
        views.ProfileDetail.as_view(),
        name='profile-detail'),

    url(r'^rides/$',
        ride_list,
        name='ride-list'),

    url(r'^rides/(?P<pk>[0-9]+)/$',
        views.RideDetail.as_view(),
        name='ride-detail'),

    url(r'^rides/(?P<pk>[0-9]+)/end/$',
        views.EndRide.as_view(),
        name='end-ride'),

    url(r'^rides/(?P<pk>[0-9]+)/passengers/$',
        views.PassengerList.as_view(),
        name='passenger-list'),

    url(r'^rides/(?P<pk>[0-9]+)/passengers/(?P<passenger_pk>[0-9]+)/$',
        views.PassengerDetail.as_view(),
        name='passenger-detail'),

    url(r'^rides/(?P<pk>[0-9]+)/requests/$',
        request_list,
        name='request-list'),

    url(r'^rides/(?P<pk>[0-9]+)/requests/(?P<id>[0-9]+)/$',
        views.RequestDetail.as_view(),
        name='request-detail'),

    url(r'^rides/(?P<pk>[0-9]+)/requests/(?P<request_pk>[0-9]+)/accept/$',
        views.AcceptRequest.as_view(),
        name='accept-request'),

    url(r'^me/cars/$',
        views.CarList.as_view(),
        name='car-list'),

    url(r'^me/cars/(?P<pk>[0-9]+)/$',
        views.CarDetail.as_view(),
        name='car-detail'),

    url(r'^me/rides_as_driver/$',
        views.UserRidesAsDriverList.as_view(),
        name='user-rides-as-driver-list'),

    url(r'^me/rides_as_passenger/$',
        views.UserRidesAsPassengerList.as_view(),
        name='user-rides-as-passenger-list'),
    
    url(r'^me/requests/$',
        views.UserRequests.as_view(),
        name='user-request-list'),

])
