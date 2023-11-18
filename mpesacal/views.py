from django.views import View
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
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

class CalculateFeeView(View):
    def get(self, request, *args, **kwargs):
        form = TransactionForm()
        return render(request, 'calculate_fee.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = TransactionForm(request.POST)
        if form.is_valid():
            transaction_type = form.cleaned_data['transaction_type']
            amount = form.cleaned_data['amount']
            fee = calculate_mpesa_fee(amount, transaction_type)
            user = request.user if request.user.is_authenticated else None
            Transaction.objects.create(user=user, amount=amount, fee=fee, transaction_type=transaction_type)
            return render(request, 'calculate_fee.html', {'form': form, 'fee': fee, 'transaction_type': transaction_type, 'amount': amount})
        return render(request, 'calculate_fee.html', {'form': form})

class TransactionHistoryView(View):
    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return render(request, 'account/login.html')
        user_transactions = Transaction.objects.filter(user=request.user).order_by('-created_at')
        paginator = Paginator(user_transactions, 10)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, 'transaction_history.html', {'page_obj': page_obj})

class TransactionDeleteView(DeleteView):
    model = Transaction
    success_url = reverse_lazy('transaction_history')
    template_name = 'transaction_confirm_delete.html'

class BulkDeleteTransactionsView(View):
    def post(self, request, *args, **kwargs):
        transaction_ids = request.POST.getlist('transaction_ids')
        Transaction.objects.filter(id__in=transaction_ids, user=request.user).delete()
        return redirect('transaction_history')
