from django import forms 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

# Form for register new users
class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
        
# Form for login users
class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)

# Form for edit user profile
class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('bio', 'birth_date', 'pronouns', 'career','is_cuvalles', 'profile_complete')

class EditBioForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('bio',)