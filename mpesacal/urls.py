from django.urls import path
from django.views.generic.base import RedirectView
from .views import calculate_fee

urlpatterns = [
    path('', RedirectView.as_view(url='https://nasonga.com'), name='home'),
    path('calculate-fee/', calculate_fee, name='calculate_fee'),
]
