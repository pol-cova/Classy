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

# import from social
from social.models import Post

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
        tasks = Task.objects.filter(user=user, completed=False)[:3]
        # count all task by user
        task_count = Task.objects.filter(user=user).count()
        # count not completed for user
        incomplete_tasks = Task.objects.filter(user=user, completed=False).count()
        # count completed tasks for user
        completed_tasks = Task.objects.filter(user=user, completed=True).count()
        # count not completed remainders
        remainders_count = Remainder.objects.filter(user=user, is_completed=False).count()
        form_task = AddTaskForm()
        
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
        
        #post count 
        post_count = Post.objects.filter(user=user).count()

        # get latest post
        posts = Post.objects.order_by('-created')[:3]

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
        #
        today = DAYS[day_name]
        # get user subjects
        subjects = Subject.objects.filter(user=user)
        # user percetange complete tasks
        if task_count > 0:
            percentage = (completed_tasks / task_count) * 100
            percentage = int(percentage)
        else:
            percentage = 0

        context = {
            'user': user,
            'tasks': tasks,
            'remainders_count': remainders_count,
            'incomplete_tasks': incomplete_tasks,
            'form_task': form_task,
            'subjects': subjects,
            'today': today,
            'notes_count': notes_count,
            'post_count' : post_count,
            'completed_tasks': completed_tasks,
            'task_count': task_count,
            'percentage': percentage,
            'posts': posts,
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
    
