from django.shortcuts import render
from .forms import AddTaskForm, EditTaskForm, AddGroupForm
from .models import Task, Group
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

@login_required(login_url='/login')
def todo(request):
    # Form for add a new task
    form_task = AddTaskForm()
    # Form for add a new group
    form_group = AddGroupForm()
    # Form for edit task
    edit_task = EditTaskForm()
    # Get if user has tasks
    tasks = Task.objects.filter(user=request.user)
    # Get if user has groups
    groups = Group.objects.filter(user=request.user)
    # active filter
    active_filter = 'Todas'
    # Context
    context = {
        'form_task': form_task,
        'edit_task': edit_task,
        'tasks': tasks,
        'form_group': form_group,
        'groups': groups,
        'active_filter': active_filter
    }

    return render(request, 'todo.html', context)

# create a new task
@login_required(login_url='/login')
def add_task(request):
    if request.method == 'POST':
        form = AddTaskForm(request.POST)
        if form.is_valid():
            # Create task
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('todo')
    return redirect('todo')

@login_required(login_url='/login')
def new_task(request):
    if request.method == 'POST':
        form = AddTaskForm(request.POST)
        if form.is_valid():
            # Create task
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('home')
    return redirect('todo')


# create a new group
@login_required(login_url='/login')
def add_group(request):
    if request.method == 'POST':
        form = AddGroupForm(request.POST)
        if form.is_valid():
            # Create group
            group = form.save(commit=False)
            group.user = request.user
            group.save()
            return redirect('home')
    return redirect('todo')

# edit a task
@login_required(login_url='/login')
def edit_task(request, task_id):
    taks = get_object_or_404(Task, id=task_id, user=request.user)
    if request.method == 'POST':
        form = EditTaskForm(request.POST, instance=taks)
        if form.is_valid():
            form.save()
            return redirect('todo')
    return redirect('todo')

# delete a task
@login_required(login_url='/login')
def delete_task(request, task_id):
    taks = get_object_or_404(Task, id=task_id, user=request.user)
    taks.delete()
    return redirect('todo')

# complete a task
@login_required(login_url='/login')
def complete_task(request, task_id):
    taks = get_object_or_404(Task, id=task_id, user=request.user)
    taks.completed = True
    taks.save()
    return redirect('home')


# decomplete a task
@login_required(login_url='/login')
def decomplete_task(request, task_id):
    taks = get_object_or_404(Task, id=task_id, user=request.user)
    taks.completed = False
    taks.save()
    return redirect('todo')

# filter tasks by group
@login_required(login_url='/login')
def filter_group(request, group_id):
    # Form for add a new task
    form_task = AddTaskForm()
    # Form for add a new group
    form_group = AddGroupForm()
    # Form for edit task
    edit_task = EditTaskForm()
    # Get if user has tasks
    tasks = Task.objects.filter(user=request.user, group=group_id)
    # Get if user has groups
    groups = Group.objects.filter(user=request.user)
    
    # active filter
    active_filter = Group.objects.get(id=group_id)
    # Context
    context = {
        'form_task': form_task,
        'edit_task': edit_task,
        'tasks': tasks,
        'form_group': form_group,
        'groups': groups,
        'active_filter': active_filter
    }

    return render(request, 'todo.html', context)

# Check task with cors
# @login_required(login_url='/login')
def check_task(request, task_id):
    response = {
        'status': 'ok',
        'task_id': task_id
    }
    return JsonResponse(response)