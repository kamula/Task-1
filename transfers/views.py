from .serializers import AccountCreationSerializer, GetAccountCreationSerializer, CreateTransferSerializer
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
  # Get Account details view
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


@swagger_auto_schema(methods=['post'], request_body=CreateTransferSerializer)
@api_view(['POST'])  # define the HTTP method of accessing the view
# The user has to be authenticated before creating an Account (before accessing the API endpoint)
@permission_classes([IsAuthenticated])
def create_transfer(request):
    '''This view initiates the transaction. It will use the Account of the logged in user.
    The view can retrieve account details by using the logged in user access Token
    '''
    resp = {}
    if request.method == 'POST':
        amount = request.data.get('amount')
        # Receivers Account (user Phone Number)
        phone_number = request.data.get('phone_number')
        if int(amount) < 0:
            resp['status'] = 'fail'
            resp['message'] = "amount cannot be less than zero"
            return Response(resp, status=status.HTTP_400_BAD_REQUEST)
        else:
            # Get the logged in user details from the access Token and also fetch the user account
            user = request.user
            sender_account = Account.objects.get(user=user.id)
            # Check if amount to be send is grater tha available balance
            if int(amount) > sender_account.starting_balance:
                resp['status'] = 'fail'
                resp['message'] = 'Transfer amount is greater than the available balance'
                return Response(resp, status=status.HTTP_400_BAD_REQUEST)
            else:
                '''if amount is not < 0 and amount is not greater than available balance:
                    1. Get receiver's account details
                    2. Save the receivers & senders details in the Transfers Table
                    3. Subtract senders Available balance and update Sender's Account
                    4. Update Receivers starting balance
                '''
                transfer_data = {}
                receiver_registered_account = User.objects.get(
                    phone_number=phone_number)
                sender_transfer_account = Account.objects.get(
                    user=receiver_registered_account.id)
                receiver_transfer_account = Account.objects.get(
                    user=request.user.id)
                transfer_data['sender_account'] = sender_transfer_account.id
                transfer_data['receiving_account'] = receiver_transfer_account.id
                transfer_data['amount'] = amount

                serializer = CreateTransferSerializer(data=transfer_data)
                if serializer.is_valid():
                    resp['status'] = 'success'
                    resp['message'] = f'Successfully Tramsfered {amount} to account {phone_number}'
                    # save the Transaction
                    serializer.save()
                    # Update Sender balance by subtracting the Transfered Amount
                    sender_transfer_account.starting_balance = sender_account.starting_balance - int(
                        amount)
                    sender_transfer_account.save()

                    # Update Receiver Amount by adding The Transfer amount
                    receiver_transfer_account.starting_balance = sender_account.starting_balance + int(
                        amount)
                    sender_transfer_account.save()
                    return Response(resp, status=status.HTTP_200_OK)
                else:
                    resp['status'] = 'fail'
                    resp['message'] = f'Trasfered {amount} to account {phone_number} is not successfull'
                    return Response(resp, status=status.HTTP_400_BAD_REQUEST)
