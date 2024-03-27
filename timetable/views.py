from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Subject
from .forms import SubjectForm

# Create your views here.
@login_required(login_url='/login')
def timetable(request):
    add_subject_form = SubjectForm()
    # Chek if user has subjects
    subjects = Subject.objects.filter(user=request.user)
    DAYS = [
        'Lunes',
        'Martes',
        'Miercoles',
        'Jueves',
        'Viernes',
        'Sabado'
    ]
    context = {
        'add_subject_form': add_subject_form,
        'subjects': subjects,
        'days': DAYS
    }
    return render(request, 'timetable.html', context)

# Create subject
@login_required(login_url='/login')
def add_subject(request):
    if request.method == "POST":
        form = SubjectForm(request.POST)
        if form.is_valid():
            subject = form.save(commit=False)
            subject.user = request.user
            subject.save()
            print('success')
            return redirect('timetable')
    else:
        form = SubjectForm()
        print('error')
    return render(request, 'timetable.html', {'add_subject_form': form})

# Delete subject
@login_required(login_url='/login')
def delete_subject(request, pk):
    subject = Subject.objects.get(id=pk)
    subject.delete()
    return redirect('timetable')