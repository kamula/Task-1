from rest_framework import serializers
from . models import User


class UserAccountSerializer(serializers.ModelSerializer):
    '''Class responsible for converting User objects into data types understandable by javascript and front-end frameworks.
        The class also provides deserialization, allowing parsed data to be converted back into complex types, after first validating the incoming data
    '''
    class Meta:
        model = User
        fields = ['full_name', 'phone_number', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self):
        '''Override the save method'''
        user = User(
            full_name=self.validated_data['full_name'],
            phone_number=self.validated_data['phone_number'],
        )
        password = self.validated_data['password']
        user.set_password(password)
        user.save()
        return user
