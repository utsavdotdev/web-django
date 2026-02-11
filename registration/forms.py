from django import forms
from .models import Registration
from django.core.validators import RegexValidator
import re


class RegistrationForm(forms.Form):
    """Registration form with comprehensive validation"""
    # Name field
    name = forms.CharField(
        max_length=100,
        # error_messages={'required': 'Name is required'}
    )


    # Email field
    email = forms.EmailField(
        error_messages={
            'required': 'Email is required',
            'invalid': 'Please enter a valid email'
        }
    )

   
    # Password field
    password = forms.CharField(
        widget=forms.PasswordInput,
        error_messages={'required': 'Password is required'}
    )

    def clean_password(self):
        """Validate password strength"""
        password = self.cleaned_data.get('password')
        # At least 8 chars, 1 uppercase, 1 lowercase, 1 digit, 1 symbol
        password_regex = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[^a-zA-Z\d\s]).{8,}$'
        if not re.match(password_regex, password):
            raise forms.ValidationError(
                'Password must be at least 8 characters long and include '
                'one uppercase letter, one lowercase letter, one number, '
                'and one symbol'
            )
        return password
