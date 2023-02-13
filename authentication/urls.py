# This section contains the URL paths for User_Registration and User_Login views (functions)

from . import views
from django.urls import path

urlpatterns = [
    path('register', views.user_registration_view, name='user_registration_view'),
]
