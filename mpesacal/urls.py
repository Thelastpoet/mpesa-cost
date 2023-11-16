from django.urls import path
from .views import calculate_fee

urlpatterns = [
    path('calculate-fee/', calculate_fee, name='calculate_fee'),
]