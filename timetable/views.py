from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Subject
from .forms import SubjectForm

# Create your views here.
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
@login_required
def add_subject(request):
    if request.method == "POST":
        form = SubjectForm(request.POST)
        if form.is_valid():
            subject = form.save(commit=False)
            subject.user = request.user
            subject.save()
            return redirect('timetable')
    else:
        form = SubjectForm()
    return redirect('timetable')

# Delete subject
@login_required
def delete_subject(request, pk):
    subject = Subject.objects.get(id=pk)
    subject.delete()
    return redirect('timetable')