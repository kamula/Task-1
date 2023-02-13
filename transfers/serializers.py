# This file contains the classes for serializing and Deserializing Accounts and Transfers Data

from rest_framework import serializers
from authentication.models import User
from . models import Account, Transfer


class AccountCreationSerializer(serializers.ModelSerializer):
    '''Class for Serializing & Deserializing  Account object'''
    class Meta:
        model = Account
        fields = ['id', 'user', 'starting_balance', 'date_created']
        read_only_fields = ['date_created']


class GetAccountCreationSerializer(serializers.ModelSerializer):
    '''Class for  Deserializing  Account object'''

    class Meta:
        model = Account
        fields = ['id', 'user', 'starting_balance', 'date_created']
        read_only_fields = ['date_created']


class CreateTransferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transfer
        fields = ['sender_account', 'receiving_account', 'amount']
