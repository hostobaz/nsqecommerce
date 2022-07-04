# modules
from rest_framework import viewsets, status
from rest_framework.response import Response
from django.db import connection

# models
from .models import BalanceAccount
from bank_account.models import BankAccount

# serializer
from balance.SerializerBalance import SerializerBalance

class ViewBalance(viewsets.ModelViewSet):
    """
    API endpoint that allows create, edit, view
    """
    queryset = BalanceAccount.objects.all()
    serializer_class = SerializerBalance

    # view transaction history
    def view_transaction(self, request, bankId):
        # check bankaccount is exists
        get_bank_account = BankAccount.objects.filter(id=bankId).first()
        if get_bank_account == None:
            return Response({'data': [], 'message':'Bank Account is not found.', 'status': status.HTTP_400_BAD_REQUEST })

        get_bank_list = BalanceAccount.objects.filter(bank_account_id=bankId).values().order_by('-created_at')

        return Response({'data': get_bank_list, 'status': status.HTTP_200_OK })
        
    # view balance
    def view_balance(self, request, bankId, *args, **kwargs):
        # check bankaccount is exists
        get_bank_account = BankAccount.objects.filter(id=bankId).first()
        if get_bank_account == None:
            return Response({'data': [], 'message':'Bank Account is not found.', 'status': status.HTTP_400_BAD_REQUEST })

        with connection.cursor() as cursor:
            cursor.execute('SELECT SUM(deposit-withdraw) AS balance from balance_balanceaccount WHERE bank_account_id= %s GROUP BY bank_account_id', [bankId])
            get_balance = cursor.fetchone()
            balance = 0 if get_balance == None else get_balance[0]

        return Response({'data': {'balance': balance}, 'status': status.HTTP_200_OK })

    # create transaction
    def create_transaction(self, request, bankId):
        # check if parameter sent completely
        serializer_balance = self.serializer_class(data=request.data)
        if serializer_balance.is_valid():
            input_serializer_balance = serializer_balance.data
        else:
            return Response({'data': [], 'message':'Your input is not sent completely. ', 'status': status.HTTP_400_BAD_REQUEST })

        # preparing input
        get_input_list = {
            "bank_id": bankId,
            "status":  str(input_serializer_balance['status']),
            "deposit": float(input_serializer_balance["deposit"]),
            "withdraw": float(input_serializer_balance["withdraw"]),
            "destination_bank_id": 0,
        }

        # check bank account is exists
        get_bank_account = BankAccount.objects.filter(id=get_input_list["bank_id"]).first()
        if get_bank_account == None:
            return Response({'data': [], 'message':'Bank Account is not found.', 'status': status.HTTP_400_BAD_REQUEST })
    
        # deposit
        if 'deposit' == get_input_list["status"]:
            if get_input_list['deposit'] == 0:
                return Response({'data': [], 'message':'Please enter amount.', 'status': status.HTTP_400_BAD_REQUEST })
            
            # insert transaction
            BalanceAccount.objects.create(
                bank_account_id = get_input_list["bank_id"], 
                deposit=get_input_list["deposit"], 
                withdraw=0.00,
                status=get_input_list["status"]
            )

            return Response({'data': [], 'message':'You have completed the transaction.', 'status': status.HTTP_201_CREATED })

        # withdraw
        if 'withdraw' == get_input_list["status"]:
            if get_input_list['withdraw'] == 0:
                return Response({'data': [], 'message':'Please enter amount.', 'status': status.HTTP_400_BAD_REQUEST })

            # check balance is enoughth
            with connection.cursor() as cursor:
                cursor.execute('SELECT SUM(deposit-withdraw) AS balance from balance_balanceaccount WHERE bank_account_id= %s GROUP BY bank_account_id', [bankId])
                get_balance = cursor.fetchone()
                current_balance = 0 if get_balance == None else get_balance[0]

            if current_balance < get_input_list["withdraw"]:
                return Response({'data': [], 'message':'Your amount is not enough.', 'status': status.HTTP_400_BAD_REQUEST })

            # insert transaction
            BalanceAccount.objects.create(
                bank_account_id = get_input_list["bank_id"], 
                deposit=0.00,
                withdraw=get_input_list["withdraw"], 
                status=get_input_list["status"]
            )

            return Response({'data': [], 'message':'You have completed the transaction.', 'status': status.HTTP_201_CREATED })

        # transfer
        if 'transfer' == get_input_list["status"]:
            # check destination bank_id
            if 'destination_bank_id' not in request.data:
                return Response({'data': [], 'message':'Please select a destination account.', 'status': status.HTTP_400_BAD_REQUEST })

            if get_input_list['withdraw'] == 0:
                return Response({'data': [], 'message':'Please enter amount.', 'status': status.HTTP_400_BAD_REQUEST })
            
            get_input_list["destination_bank_id"] = int(request.data['destination_bank_id'])

            # check balance is enough
            with connection.cursor() as cursor:
                cursor.execute('SELECT SUM(deposit-withdraw) AS balance from balance_balanceaccount WHERE bank_account_id= %s GROUP BY bank_account_id', [bankId])
                get_balance = cursor.fetchone()
                current_balance = 0 if get_balance == None else get_balance[0]

            if current_balance < get_input_list["withdraw"]:
                return Response({'data': [], 'message':'Your amount is not enough', 'status': status.HTTP_400_BAD_REQUEST })

            # check bank account destination is exists
            get_bank_account = BankAccount.objects.filter(id=get_input_list["destination_bank_id"]).first()
            if get_bank_account == None:
                return Response({'data': [], 'message':'Bank Account destination is not found.', 'status': status.HTTP_400_BAD_REQUEST })

            # source
            BalanceAccount.objects.create(bank_account_id = bankId, deposit=0.00, withdraw=get_input_list["withdraw"], status=get_input_list["status"])
            # target
            BalanceAccount.objects.create(bank_account_id = get_input_list["destination_bank_id"], deposit=get_input_list["withdraw"], withdraw=0.00, status=get_input_list["status"])

            return Response({'data': [], 'message':'You have completed the transaction.', 'status': status.HTTP_201_CREATED })

        return Response({'data': [], 'message':'Invalid information, please try again.', 'status': status.HTTP_400_BAD_REQUEST })