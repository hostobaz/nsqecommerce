# modules
from rest_framework import viewsets

# models
from customer.models import Customer

# serializer
from customer.SerializerCustomer import SerializerCustomer

class ViewCustomer(viewsets.ModelViewSet):
    """
    API endpoint that allows create, edit, view
    """
    queryset = Customer.objects.all()
    serializer_class = SerializerCustomer
