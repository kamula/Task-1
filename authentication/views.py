from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework.decorators import api_view
from . serializers import UserAccountSerializer, UserLoginSerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .utils import get_tokens_for_user, get_account_from_phone_number


@swagger_auto_schema(methods=['post'], request_body=UserAccountSerializer)
@api_view(['POST'])  # define the HTTP method of accessing the view
def user_registration_view(request):
    '''Interface that receive a web request and return a web response to the frontend clients for user registration'''
    resp = {}
    if request.method == 'POST':
        # Get the data obtained from the request.POST HTTP method
        serializer = UserAccountSerializer(data=request.data)
        # check if the data passed via the POST request is valid
        # If the serializer (validator is valid): save the data and return a success message else return an error message
        if serializer.is_valid():
            serializer.save()
            resp['message'] = 'success'
            return Response(resp, status=status.HTTP_201_CREATED)
        else:
            resp['message'] = serializer.errors
            return Response(resp, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(methods=['post'], request_body=UserLoginSerializer)
@api_view(['POST'])
def login_view(request):
    '''User Login function'''
    # if the user login credentials are valid and the user details exist in the database, authernticate the user and return an access and refresh tokens else return an error message
    # The access token will be used to allow the user to access the API endpoints
    resp = {}
    if request.method == 'POST':
        phone_number = request.data.get('phone_number')
        password = request.data.get('password')
        user_account = get_account_from_phone_number(phone_number)
        if user_account:
            authenticate(user_account, password=password)
            token = get_tokens_for_user(user_account)
            resp['message'] = 'successfully logged in'
            resp['token'] = token
            return Response(resp, status=status.HTTP_200_OK)
        else:
            print(user_account)
            resp['message'] = 'invalid login credentials'
            return Response(resp, status=status.HTTP_400_BAD_REQUEST)
