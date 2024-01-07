from django.shortcuts import render, redirect
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
# import forms
from .forms import SignUpForm, LoginForm
# index 
def index(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = LoginForm()
        return render(request, 'index.html', {'form': form})
    
def home(request):
    return render(request, 'home.html')

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            # get form data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            # authenticate user
            user = authenticate(request, username=username, password=password)
            if user:
                # login user
                login(request, user)
                return redirect('home')
        else:
            return redirect('index')

