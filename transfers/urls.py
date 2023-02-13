# This section contains the URL paths for Account Creation and Account Transfers views (functions)
from django.urls import path
from . import views

urlpatterns = [
    path('accounts', views.create_account_view, name='create_account_view'),
]
