from django import forms
from .models import Subject

class SubjectForm(forms.ModelForm):
    HOURS_CHOICES = [(f"{i:02d}:00", f"{i:02d}:00") for i in range(8, 19)]  # Choices from 8:00 to 18:00

    hour_start = forms.ChoiceField(choices=HOURS_CHOICES, label='Hora de inicio',
                                    widget=forms.Select(attrs={'class': 'form-control'}))
    hour_end = forms.ChoiceField(choices=HOURS_CHOICES, label='Hora de fin',
                                  widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = Subject
        fields = ('name', 'teacher', 'clasroom', 'hour_start', 'hour_end', 'day', 'color')
        labels = {
            'name': 'Nombre',
            'teacher': 'Profesor',
            'clasroom': 'Aula',
            'day': 'Dia',
            'color': 'Color',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'teacher': forms.TextInput(attrs={'class': 'form-control'}),
            'clasroom': forms.TextInput(attrs={'class': 'form-control'}),
            'day': forms.Select(attrs={'class': 'form-control'}),
            'color': forms.Select(attrs={'class': 'form-control'}),
        }
