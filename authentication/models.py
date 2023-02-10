import uuid
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class User(AbstractBaseUser):
    '''This class is responsible for creating the Users table in the database.

        The database attributes are: id, full_name, phone_number, date_joined,
        date_updated, last_login, is_admin, is_active, is_staff, is_superuser
    '''

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    full_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15, unique=True)

    # Required fields by django to create a custom User model
    date_joined = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'phone_number'  # login field
    # field required to create an a User account
    REQUIRED_FIELDS = ['full_name']

    def __str__(self) -> str:
        '''returns a human-readable, string representation of the User Class'''
        return self.full_name

    def has_perm(self, perm, obj=None):
        return self.is_admin

    # Does this user have permission to view this app?
    def has_module_perms(self, app_label):
        return True
