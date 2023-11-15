from django import forms
from django.core.exceptions import ValidationError
from .models import Transaction

def validate_amount(value):
    if value < 1 or value > 250000:
        raise ValidationError('The amount must be between 1 and 250,000 Kenyan Shillings.')

class TransactionForm(forms.ModelForm):
    amount = forms.DecimalField(validators=[validate_amount])

    class Meta:
        model = Transaction
        fields = ['amount', 'transaction_type']
