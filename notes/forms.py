from django import forms
from .models import Note

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'subject', 'content']
        labels = {'title': 'Titulo', 'subject': 'Materia', 'content': 'Apunte'}
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'subject': forms.Select(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'cols': 80}),
        }