from django import forms
from .models import Remainder

class ReminderForm(forms.ModelForm):
    class Meta:
        model = Remainder
        fields = ['title', 'detail', 'date', 'time', 'is_important']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'detail': forms.Textarea(attrs={'class': 'form-control'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'is_important': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
        labels = {
            'title': 'Titulo',
            'detail': 'Detalles',
            'date': 'Fecha',
            'time': 'Tiempo',
            'is_important': 'Importante',
        }