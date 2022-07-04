# modules
from django.db import models

# models
from customer.models import Customer

# for creating uuid
import uuid

class BankAccount(models.Model):
        # random Unique
        def randomUnique():
                return str(uuid.uuid4().hex[:20].upper())

        account_number = models.CharField(max_length=20, default=randomUnique)
        customer = models.ForeignKey(Customer,on_delete=models.DO_NOTHING)
        created_at = models.DateTimeField(auto_now_add=True)

        def __str__(self):
                return self.account_number

