from django.contrib.auth.models import User
from django.db import models

class MpesaFee(models.Model):
    TRANSACTION_TYPES = [
        ('registered_users', 'Send to another M-Pesa'),
        ('agent_withdrawal', 'Withdraw from agent'),
        ('unregistered_users', 'Send to unregistered user'),
        ('atm_withdrawal', 'ATM withdrawal'),
        ('other_network_users', 'Send to another network')
    ]
    transaction_type = models.CharField(max_length=255, choices=TRANSACTION_TYPES)
    min_amount = models.DecimalField(max_digits=10, decimal_places=2)
    max_amount = models.DecimalField(max_digits=10, decimal_places=2)
    fee = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.transaction_type} ({self.min_amount}-{self.max_amount}): {self.fee}'

class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    fee = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_type = models.CharField(max_length=255, choices=MpesaFee.TRANSACTION_TYPES, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Transaction by {self.user.username} of {self.amount} with fee {self.fee} on {self.created_at}'
