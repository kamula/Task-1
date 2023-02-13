# This file contains the classes for serializing and Deserializing Accounts and Transfers Data

from rest_framework import serializers
from . models import Account



class AccountCreationSerializer(serializers.ModelSerializer):
    '''Class for Serializing & Deserializing  Account object'''
    class Meta:
        model = Account
        fields = ['id','user', 'starting_balance', 'date_created']
        read_only_fields = ['date_created']


