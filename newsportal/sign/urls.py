from django.urls import path
from django.contrib.auth.views import *

from .views import BaseRegisterView, IndexView, upgrade_me

urlpatterns = [
    path('login/',
         LoginView.as_view(template_name='sign/login.html'),
         name='login'),
    path('logout/',
         LogoutView.as_view(template_name='sign/logout.html'),
         name='logout'),
    path('', IndexView.as_view()),
    path('signup/', BaseRegisterView.as_view(template_name='sign/signup.html'),
         name='sign_signup'),
    path('upgrade/', upgrade_me, name='upgrade'),

]
