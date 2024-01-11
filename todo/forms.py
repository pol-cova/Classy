# Create form for todo app
from django import forms
from .models import Task, Group
# Create form for add a new task
class AddTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'group']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Titulo'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Descripcion'}),
            'group': forms.Select(attrs={'class': 'form-control'}),
        }

# Create form for add a new group
class AddGroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['title']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Titulo'}),
        }