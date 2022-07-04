# modules
from rest_framework import viewsets

# models
from bank_account.models import BankAccount

# serializer
from bank_account.SerializerBankAccount import SerializerBankAccount

class ViewBankAccount(viewsets.ModelViewSet):
    """
    API endpoint that allows create, edit, view
    """
    queryset = BankAccount.objects.all()
    serializer_class = SerializerBankAccount
