from django.shortcuts import render
from django.core.exceptions import ValidationError
from .models import Transaction, MpesaFee
from .forms import TransactionForm

def load_mpesa_fees(transaction_type):
    fees = MpesaFee.objects.filter(transaction_type=transaction_type)
    return [(fee.min_amount, fee.max_amount, fee.fee) for fee in fees]

def calculate_mpesa_fee(amount, transaction_type):
    fees = load_mpesa_fees(transaction_type)
    for min_amount, max_amount, fee in fees:
        if min_amount <= amount <= max_amount:
            return fee
    return 0

def calculate_fee(request):
    transaction_type = None  
    transaction_type_descriptions = {
        'registered_users': 'Sending to Registered M-Pesa Users',
        'agent_withdrawal': 'Withdrawing from an Agent',
        'unregistered_users': 'Sending to Unregistered Users',
        'other_network_users': 'Sending to Other Networks',
        'atm_withdrawal': 'ATM Withdrawal',
    }
    fee = None  
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            transaction_type = form.cleaned_data['transaction_type']
            fee = calculate_mpesa_fee(form.cleaned_data['amount'], transaction_type)
            user = request.user if request.user.is_authenticated else None
            Transaction.objects.create(user=user, amount=form.cleaned_data['amount'], fee=fee, transaction_type=transaction_type)            
    else:
        form = TransactionForm()
    transaction_type_description = transaction_type_descriptions[transaction_type] if transaction_type else None
    return render(request, 'mpesacal/calculate_fee.html', {'form': form, 'fee': fee, 'transaction_type': transaction_type_description})
