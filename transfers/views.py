from .serializers import AccountCreationSerializer
from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework.decorators import api_view
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

@swagger_auto_schema(methods=['post'], request_body=AccountCreationSerializer)
@api_view(['POST'])  # define the HTTP method of accessing the view
def create_account_view(request):
    '''Function for Creating Account'''
    resp = {}
    return Response(resp, status=status.HTTP_400_BAD_REQUEST)