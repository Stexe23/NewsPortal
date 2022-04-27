from django.urls import path

from newsportal.users.views import profile, change_profile


urlpatterns = [
    path(r'^profile/$', profile, name='profile'),
    path(r'^profile/change/$', change_profile, name='change_profile'),
]
