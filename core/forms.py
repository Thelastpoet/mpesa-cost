from allauth.account.forms import SignupForm
from django import forms

class CustomSignupForm(SignupForm):
    def clean_password1(self):
        return self.cleaned_data.get('password1')