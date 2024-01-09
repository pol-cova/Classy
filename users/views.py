from django.shortcuts import render, redirect
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth import authenticate, login, logout
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

# dashboard
def home(request):
    if request.user.is_authenticated:
        user = request.user
        return render(request, 'home.html', {'user': user})
    else:
        return render(request, 'index.html', {'message': 'Inicia sesión para continuar...'})

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
                return render(request, 'index.html', {'message': 'Usuario o contraseña incorrectos'})
        else:
            return redirect('index')

def user_signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            # save user
            form.save()
            return render(request, 'index.html', {'message': 'Usuario creado exitosamente'})
        else:
            return redirect('index')

def user_logout(request):
    logout(request)
    return redirect('index')

def user_profile(request):
    if request.user.is_authenticated:
        user = request.user
        return render(request, 'profile.html', {'user': user})
    else:
        return render(request, 'index.html', {'message': 'Inicia sesión para continuar...'})