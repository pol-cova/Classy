from .models import Post, Comment
from django import forms

# PostForm
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content',)
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
        }
        labels = {
            'title': 'Titulo',
            'content': 'Contenido',
        }

# CommentForm
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)
        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control mr-2', 'rows': 1, 'cols': 50, 'placeholder': 'Escribe un comentario...'}),
        }
        labels = {
            'content': '',
        }
