from django.shortcuts import render, redirect
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import datetime
import pytz
# Mail settings
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.html import strip_tags

# import user model
from django.contrib.auth.models import User

# import forms
from .forms import SignUpForm, LoginForm, EditProfileForm, EditBioForm
from .models import Profile

# import from todo
from todo.models import Task
from todo.forms import AddTaskForm

# import from timetable
from timetable.models import Subject

# import from remainders
from remainders.models import Remainder

# import from notes
from notes.models import Note


# index 
def index(request):
    if request.user.is_staff:
        return redirect('support_tickets')
    elif request.user.is_authenticated:
        return redirect('home')
    else:
        form = LoginForm()
        return render(request, 'index.html', {'form': form})

# dashboard
def home(request):
    if request.user.is_staff:
        return redirect('support_tickets')
    elif request.user.is_authenticated:
        user = request.user
        tasks = Task.objects.filter(user=user)
        # count not completed for user
        tasks_count = Task.objects.filter(user=user, completed=False).count()
        # count not completed remainders
        remainders_count = Remainder.objects.filter(user=user, is_completed=False).count()
        form_task = AddTaskForm()
        # get user subjects
        subjects = Subject.objects.filter(user=user)
        # get user notes
        notes_count = Note.objects.filter(owner=user).count()
        # timezone
        tz = pytz.timezone('America/Mexico_City')
        # todays date
        today = datetime.datetime.now(tz=tz)
        # get day of week
        day = today.weekday()
        # get day name
        day_name = today.strftime("%A")

        # days dict key:value -> day_name: spanish_name
        DAYS = {
            'Monday': 'Lunes',
            'Tuesday': 'Martes',
            'Wednesday': 'Miercoles',
            'Thursday': 'Jueves',
            'Friday': 'Viernes',
            'Saturday': 'Sabado',
            'Sunday': 'Domingo',
        }
        context = {
            'user': user,
            'tasks': tasks,
            'remainders_count': remainders_count,
            'tasks_count': tasks_count,
            'form_task': form_task,
            'subjects': subjects,
            'today': DAYS[day_name],
            'notes_count': notes_count,
        }
        return render(request, 'home.html', context)
    else:
        return render(request, 'index.html', {'message': 'Inicia sesión para continuar...'})

# login page render
def login_page(request):
    return render(request, 'login.html')
# user login
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
                # create user profile 
                profile, created = Profile.objects.get_or_create(user=user)
                return redirect('home')
            else:
                return render(request, 'login.html', {'message': 'Usuario o contraseña incorrectos, intenta de nuevo...'})
        else:
            return redirect('index')

# user signup page
def signup_page(request):
    form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

# user signup
def user_signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            username = form.cleaned_data['username']
            # save user
            form.save()
            # send an email to complete profile
            context = {
                'message': "Hola @" + username + "! Gracias por registrarte en Classy"
            }

            html_message = render_to_string('email.html', context=context)
            plain_message = strip_tags(html_message)
            subject = "noreply: Classy | Completa tu perfil ahora"
            body = plain_message
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [email]
            msg = EmailMultiAlternatives(subject, body, email_from, recipient_list)
            msg.attach_alternative(html_message, "text/html")
            msg.send()
            return redirect('login_page')
        else:
            form = SignUpForm()
            context = {
                'form': form,
                'message': 'Error al crear usuario, intenta de nuevo...'
            }
            return render(request, 'signup.html', context)

# user logout
def user_logout(request):
    logout(request)
    return redirect('index')

# user profile
def user_profile(request):
    if request.user.is_authenticated:
        user = request.user
        profile = request.user.profile
        PRONOUNS = (
        ('SHE', 'She/Her'),
        ('HE', 'He/Him'),
        ('THEY', 'They/Them'),
        ('OTHER', 'Other'),
        )
        context = {
            'user': user,
            'PRONOUNS': PRONOUNS,
            'profile': profile,
        }
        return render(request, 'profile.html', context)
    else:
        return render(request, 'index.html', {'message': 'Inicia sesión para continuar...'})

# complete profile
def complete_profile(request):
    if request.user.is_authenticated:
        userProfile, created = Profile.objects.get_or_create(user=request.user)
        form = EditProfileForm(instance=userProfile)
        if request.method == 'POST':
            form = EditProfileForm(request.POST, instance=userProfile)
            if form.is_valid():
                form.save()
                return redirect('profile')
            else:
                return redirect('profile')
    else:
        return render(request, 'index.html', {'message': 'Inicia sesión para continuar...'})

# edit bio
def edit_profile(request):
    if request.user.is_authenticated:
        userProfile, created = Profile.objects.get_or_create(user=request.user)
        form = EditBioForm(instance=userProfile)
        if request.method == 'POST':
            form = EditBioForm(request.POST, instance=userProfile)
            if form.is_valid():
                form.save()
                return redirect('profile')
            else:
                return redirect('profile')
    else:
        return render(request, 'index.html', {'message': 'Inicia sesión para continuar...'})

# delete account 
def delete_account(request):
    if request.user.is_authenticated:
        user = request.user
        user.delete()
        return redirect('index')
    else:
        return render(request, 'index.html', {'message': 'Inicia sesión para continuar...'})
    
# forgot password
def forgot_password(request):
    return render(request, 'forgot-password.html')