from .serializers import AccountCreationSerializer
from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework.decorators import api_view
from drf_yasg.utils import swagger_auto_schema
from rest_framework.permissions import IsAuthenticated
from drf_yasg import openapi
from rest_framework.decorators import api_view, permission_classes


@swagger_auto_schema(methods=['post'], request_body=AccountCreationSerializer)
@api_view(['POST'])  # define the HTTP method of accessing the view
# The user has to be authenticated before creating an Account (before accessing the API endpoint)
@permission_classes([IsAuthenticated])
def create_account_view(request):
    '''Account creation endpoint. Pass the access token on the request headers'''
    resp = {}
    if request.method == 'POST':
        # Get user from the access Token and starting_balance from request Body
        user = request.user
        starting_balance = request.data.get('starting_balance')
        if int(starting_balance) < 0:
            # Check if starting balance is less than 0: If less than 0 return an error response message else create an account
            resp['status'] = 'fail'
            resp['message'] = 'Starting Balance cannot be less than 0'
            return Response(resp, status=status.HTTP_400_BAD_REQUEST)
        else:
            data = {}
            data['user'] = user.id
            data['starting_balance'] = starting_balance
            serializer = AccountCreationSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                resp['status'] = 'success'
                resp['message'] = 'Account Successfully created'
                return Response(resp, status=status.HTTP_201_CREATED)
            else:               
                resp['status'] = 'fail'
                resp['message'] = 'Account Creation Failed'
                return Response(resp, status=status.HTTP_400_BAD_REQUEST)
