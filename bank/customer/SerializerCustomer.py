# modules
from rest_framework import serializers

# models
from customer.models import Customer

class SerializerCustomer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'