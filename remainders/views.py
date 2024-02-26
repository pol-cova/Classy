from django.shortcuts import render, redirect

from .forms import ReminderForm
from .models import Remainder
# login required
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='/login')
def index(request):
    # get user remainders
    remainders = Remainder.objects.filter(user=request.user)
    form = ReminderForm()
    context = {
        'form_remainder': form,
        'remainders': remainders
    }
    return render(request, 'remainders.html', context)

# create remainder
@login_required(login_url='/login')
def create_remainder(request):
    if request.method == 'POST':
        form = ReminderForm(request.POST)
        if form.is_valid():
            form.save()
            form = ReminderForm()
            return redirect('remainders')
    else:
        form = ReminderForm()
    context = {
        'form_remainder': form
    }
    return redirect('remainders')

# complete remainder
@login_required(login_url='/login')
def complete_remainder(request, remainder_id):
    remainder = Remainder.objects.get(pk=remainder_id)
    remainder.is_completed = True
    remainder.save()
    return redirect('remainders')

# uncomplete remainder
@login_required(login_url='/login')
def uncomplete_remainder(request, remainder_id):
    remainder = Remainder.objects.get(pk=remainder_id)
    remainder.is_completed = False
    remainder.save()
    return redirect('remainders')

# delete remainder
@login_required(login_url='/login')
def delete_remainder(request, remainder_id):
    remainder = Remainder.objects.get(pk=remainder_id)
    remainder.delete()
    return redirect('remainders')

# update remainder
@login_required(login_url='/login')
def update_remainder(request, remainder_id):
    remainder = Remainder.objects.get(pk=remainder_id)
    form = ReminderForm(instance=remainder)
    if request.method == 'POST':
        form = ReminderForm(request.POST, instance=remainder)
        if form.is_valid():
            form.save()
            return redirect('remainders')
    context = {
        'form_remainder': form
    }
    return redirect('remainders')