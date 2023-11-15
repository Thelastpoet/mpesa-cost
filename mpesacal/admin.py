from django.contrib import admin
from .models import Transaction, MpesaFee

class TransactionAdmin(admin.ModelAdmin):
    list_display = ['user', 'amount', 'fee', 'transaction_type', 'created_at']

admin.site.register(Transaction, TransactionAdmin)
admin.site.register(MpesaFee)
