from django import forms
from .models import *

class AdminForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'description', 'date', 'time', 'location', 'ticket_price']
        help_texts = {
            'title': '',
            'description': '',
            'location': '',
            'ticket_price': 'Enter the price for tickets'
        }
