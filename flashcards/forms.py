from django import forms
from .models import Card, CardGroup

# Form for creating a gruop of cards
class CardGroupForm(forms.ModelForm):
    class Meta:
        model = CardGroup
        fields = ['name', 'subject', 'description']
        labels = {
            'name': 'Nombre del Grupo',
            'subject': 'Materia',
            'description': 'Descripción'
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'subject': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'})
        }

# Form for creating a card
class CardForm(forms.ModelForm):
    class Meta:
        model = Card
        fields = ['question', 'answer']
        labels = {
            'question': 'Pregunta',
            'answer': 'Respuesta'
        }
        widgets = {
            'question': forms.TextInput(attrs={'class': 'form-control'}),
            'answer': forms.TextInput(attrs={'class': 'form-control'})
        }
