# This file contains functions that provide extra utilities for the transfers app
from . models import Account


def get_account_from_account_id(account_id):
    '''Get account from user's phone number
    if account is null return None else return the account details
    '''
    account = None
    try:
        account = Account.objects.get(id=id)
    except account.DoesNotExist:
        return None
    if account != None:
        return account
