from django.urls import path
from django.views.generic.base import RedirectView
from .views import CalculateFeeView, TransactionHistoryView, BulkDeleteTransactionsView

urlpatterns = [
    path('', RedirectView.as_view(url='https://nasonga.com'), name='home'),
    path('calculate-fee/', CalculateFeeView.as_view(), name='calculate_fee'),
    path('transaction-history/', TransactionHistoryView.as_view(), name='transaction_history'),
    path('transactions/bulk_delete/', BulkDeleteTransactionsView.as_view(), name='bulk_delete_transactions'),
]
