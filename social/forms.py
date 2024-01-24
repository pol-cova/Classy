from .models import Post, Comment
from django import forms

# PostForm
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text',)
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'text': forms.Textarea(attrs={'class': 'form-control'})
        }

# CommentForm
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)
        widgets = {
            'text': forms.Textarea(attrs={'class': 'form-control'})
        }