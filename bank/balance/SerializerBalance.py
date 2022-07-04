# modules
from rest_framework import serializers

# models
from balance.models import BalanceAccount

class SerializerBalance(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BalanceAccount
        fields = ['deposit', 'withdraw', 'status']
