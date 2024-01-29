from django import forms
from .models import Ticket

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['name', 'email', 'report']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa tu nombre: '}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa tu correo:'}),
            'report': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Ingresa el problema:'}),
        }
        labels = {
            'name': 'Nombre',
            'email': 'Correo electrónico',
            'report': 'Problema',
        }

