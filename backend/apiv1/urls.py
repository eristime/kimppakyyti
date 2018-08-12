from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from apiv1 import views


urlpatterns = format_suffix_patterns([
    url(r'^$', views.api_root),
    url(r'^users/$',
        views.UserList.as_view(),
        name='user-list'),
    url(r'^users/(?P<pk>[0-9]+)/$',
        views.UserDetail.as_view(),
        name='user-detail'),

    url(r'^profiles/$',
        views.ProfileList.as_view(),
        name='profile-list'),
    url(r'^profiles/(?P<pk>[0-9]+)/$',
        views.ProfileDetail.as_view(),
        name='profile-detail'),

    url(r'^rides/$',
        views.RideList.as_view(),
        name='ride-list'),
    url(r'^rides/(?P<pk>[0-9]+)/$',
        views.RideDetail.as_view(),
        name='ride-detail'),

    url(r'^cars/$',
        views.CarList.as_view(),
        name='car-list'),
    url(r'^cars/(?P<pk>[0-9]+)/$',
        views.CarDetail.as_view(),
        name='car-detail'),
    
    #url(r'^message/$',
    #    views.MessageList.as_view(),
    #    name='message-list'),
    #url(r'^message/(?P<pk>[0-9]+)/$',
    #    views.MessageDetail.as_view(),
    #    name='message-detail'),
])
