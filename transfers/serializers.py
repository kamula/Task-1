# This file contains the classes for serializing and Deserializing Accounts and Transfers Data

from rest_framework import serializers
from . models import Account


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['user', 'starting_balance', 'date_created']
