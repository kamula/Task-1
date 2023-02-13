from .serializers import AccountCreationSerializer, GetAccountCreationSerializer
from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework.decorators import api_view
from drf_yasg.utils import swagger_auto_schema
from rest_framework.permissions import IsAuthenticated
from drf_yasg import openapi
from authentication.models import User
from . models import Account
from . utils import get_account_from_account_id
from rest_framework.decorators import api_view, permission_classes


@swagger_auto_schema(methods=['post'], request_body=AccountCreationSerializer)
@api_view(['POST'])  # define the HTTP method of accessing the view
# The user has to be authenticated before creating an Account (before accessing the API endpoint)
@permission_classes([IsAuthenticated])
def create_account_view(request):
    '''Account creation endpoint. Pass the access token on the request headers
        One user = One Account
    '''
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
                account = serializer.save()
                account_serializer = AccountCreationSerializer(account)
                resp['status'] = 'success'
                resp['message'] = 'Account Successfully created'
                resp['account'] = account_serializer.data
                return Response(resp, status=status.HTTP_201_CREATED)
            else:
                resp['status'] = 'fail'
                resp['message'] = 'Account Creation Failed'
                return Response(resp, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(methods=['get'])
@api_view(['GET'])  # define the HTTP method of accessing the view
# The user has to be authenticated before creating an Account (before accessing the API endpoint)
@permission_classes([IsAuthenticated])
def get_account_details(request, id):
    print(id)
    resp = {}
    # account = get_account_from_account_id(id)
    account = Account.objects.get(id=id)
    if account:
        account_serializer = GetAccountCreationSerializer(account)
        account_data = account_serializer.data
        account_data['user'] = User.objects.get(id=account.user.id).full_name
        resp['status'] = 'success'
        resp['account'] = account_data
        return Response(resp, status=status.HTTP_200_OK)
    else:
        resp['status'] = 'fail'
        resp['message'] = 'account not found'
        return Response(resp, status=status.HTTP_404_NOT_FOUND)
