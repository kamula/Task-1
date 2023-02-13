from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework.decorators import api_view
from . serializers import UserAccountSerializer, UserLoginSerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


@swagger_auto_schema(methods=['post'], request_body=UserAccountSerializer)
@api_view(['POST'])  # define the HTTP method of accessing the view
def user_registration_view(request):
    '''Interface that receive a web request and return a web response to the frontend clients for user registration'''
    resp = {}
    if request.method == 'POST':
        # Get the data obtained from the request.POST HTTP method
        serializer = UserAccountSerializer(data=request.data)
        # check id the data passed via the POST request is valid
        if serializer.is_valid():
            resp['message'] = 'success'
            return Response(resp, status=status.HTTP_201_CREATED)
        else:
            resp['message'] = serializer.errors
            return Response(resp, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(methods=['post'], request_body=UserLoginSerializer)
@api_view(['POST'])
def login_view(request):
    '''User Login function'''
    resp = {}
    if request.method == 'POST':
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            resp['message'] = 'success'
            return Response(resp, status=status.HTTP_200_OK)
        else:
            resp['message'] = 'please provide login credentials'
            return Response(resp, status=status.HTTP_400_BAD_REQUEST)
