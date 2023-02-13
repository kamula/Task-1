# This file contains functions that provide extra utilities for the project
from . models import User
from rest_framework_simplejwt.tokens import RefreshToken


def get_account_from_phone_number(phone_number):
    '''Get account from user's phone number
    if account is null return None else return the user account details
    '''
    account = None
    try:
        account = User.objects.get(phone_number=phone_number)
    except User.DoesNotExist:
        return None
    if account != None:
        return account

# function that generates access & refresh tokens for successfully logged in user


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }
