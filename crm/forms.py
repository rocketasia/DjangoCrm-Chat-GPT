from django import forms
from .models import Customer

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['firstname', 'surname', 'email', 'phone']  # List all the fields you want from the model
