# modules
from django.db import models

# models
from bank_account.models import BankAccount

class BalanceAccount(models.Model):
        bank_account = models.ForeignKey(BankAccount,on_delete=models.DO_NOTHING)
        deposit = models.DecimalField(max_digits=18, decimal_places=8)
        withdraw = models.DecimalField(max_digits=18, decimal_places=8)
        status = models.CharField(max_length=25)
        created_at = models.DateTimeField(auto_now_add=True)