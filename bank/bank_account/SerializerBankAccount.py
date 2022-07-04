# modules
from rest_framework import serializers

# models
from bank_account.models import BankAccount

class SerializerBankAccount(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BankAccount
        fields = ['url', 'customer']
