# This section contains the URL paths for Account Creation and Account Transfers views (functions)
from django.urls import path
from . import views

# Paths to map URL view functions
urlpatterns = [
    path('accounts', views.create_account_view, name='create_account_view'),
    path('accounts/<uuid:id>', views.get_account_details,
         name='get_account_details'),
    path('transfer', views.create_transfer, name='create_transfer'),
]
