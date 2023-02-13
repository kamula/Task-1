import uuid
from django.db import models
from django.utils import timezone
from authentication.models import User


class Account(models.Model):
    '''A class that creates an Account for a user, The class has the following attributes:
    1. id = (unique account ID)
    2. Users foreign Key (Represents the owner of the account)
    3. starting balance
    4. Date created (Time when the account was created. This field is not editable)
    5. Date Updated (Time when the account was updated. This field is editable)
    '''
    # The models allows the user to only create one account
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    starting_balance = models.IntegerField()
    date_created = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        '''returns a human-readable, string representation of the Account's Class: Account Owner full name'''
        return f'{self.user.full_name}'


class Transfer(models.Model):
    '''Class Responsible for storing all Transactions'''
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # Account sending money Reference key
    sender_account = models.ForeignKey(
        Account, on_delete=models.CASCADE, related_name='sender')
    # Account receiving money Reference key
    receiving_account = models.ForeignKey(
        Account, on_delete=models.CASCADE, related_name='receiver')
    # amount transfered from sender to receiver
    amount = models.IntegerField(default=0)
    date_created = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        '''returns a human-readable, string representation of the Account that send the money: Account Owner full name'''
        return f'{self.sender.full_name}'
