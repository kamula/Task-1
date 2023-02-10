import uuid
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class UserManager(BaseUserManager):
    '''This class allows us to add extra Manager methods to the User creation class and validation attributes'''

    def create_user(self, full_name, phone_number, password=None):
        '''validate whether user attributes are not empty before creating a user'''
        if not full_name:
            return ValueError('Full name required')
        if not phone_number:
            return ValueError('Phone number required')
        user = self.model(
            full_name=full_name,
            phone_number=phone_number
        )
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_superuser(self, full_name, phone_number, password):
        '''custom API admin creation method'''
        user = self.create_user(
            full_name=full_name,
            password=password
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


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
