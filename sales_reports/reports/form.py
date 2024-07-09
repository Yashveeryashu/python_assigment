from django import forms
from .models import EmailAddress

class EmailAddressForm(forms.ModelForm):
    class Meta:
        model = EmailAddress
        fields = ['email']
