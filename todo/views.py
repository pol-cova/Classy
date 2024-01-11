from django.shortcuts import render
from .forms import AddTaskForm, AddGroupForm
from .models import Task, Group
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
# Create your views here.
def todo(request):
    # Create form for add a new task
    form_task = AddTaskForm()
    # Create form for add a new group
    form_group = AddGroupForm()
    # Get if user has tasks
    tasks = Task.objects.filter(user=request.user)
    # Context
    context = {
        'form_task': form_task,
        'form_group': form_group,
        'tasks': tasks
    }

    return render(request, 'todo.html', context)

# create a new task
@login_required
def add_task(request):
    if request.method == 'POST':
        form = AddTaskForm(request.POST)
        if form.is_valid():
            # Create task
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('todo')
    else:
        form = AddTaskForm()
    return render(request, 'todo.html', {'form': form})