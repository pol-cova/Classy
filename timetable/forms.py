from django import forms
from .models import Subject

class SubjectForm(forms.ModelForm):
    hour_start = forms.ChoiceField(choices=[(f"{i:02d}:00", f"{i:02d}:00") for i in range(8, 19)], 
                                    widget=forms.Select(attrs={'class': 'form-control'}), 
                                    label='Hora de inicio')
    hour_end = forms.ChoiceField(choices=[(f"{i:02d}:00", f"{i:02d}:00") for i in range(8, 19)],
                                    widget=forms.Select(attrs={'class': 'form-control'}), 
                                    label='Hora de fin')

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
