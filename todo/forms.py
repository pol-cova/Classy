# Create form for todo app
from django import forms
from .models import Task, Group
# Create form for add a new task
class AddTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description','group', 'limit_date']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Titulo'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Descripcion'}),
            'group': forms.Select(attrs={'class': 'form-control'}),
            'limit_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }

# Create form for add a new group
class AddGroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}),
        }
# form for edit a task
class EditTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }