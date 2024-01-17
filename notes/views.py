from django.shortcuts import render, redirect
from .forms import NoteForm
from .models import Note

# Subject model
from timetable.models import Subject

# Create your views here.
def notes(request):
    form = NoteForm()
    # get user subjects
    subjects = Subject.objects.filter(user=request.user)
    # get user notes
    notes = Note.objects.filter(owner=request.user)
    context = {
        'form': form,
        'subjects': subjects,
        'notes': notes,}
    return render(request, 'notes.html', context)

# add_note
def add_note (request):
    if request.method != 'POST':
        # no data submitted; create a blank form
        form = NoteForm()
    else:
        # POST data submitted; process data
        form = NoteForm(data=request.POST)
        if form.is_valid():
            new_note = form.save(commit=False)
            new_note.owner = request.user
            new_note.subject = Subject.objects.get(id=request.POST['subject'])
            new_note.save()
            return redirect('notes')
    # display a blank or invalid form
    context = {'form': form}
    return render(request, 'note.html', context)

# edit_note
def edit_note (request, note_id):
    note = Note.objects.get(id=note_id)
    if request.method != 'POST':
        # initial request; pre-fill form with the current note
        form = NoteForm(instance=note)
    else:
        # POST data submitted; process data
        form = NoteForm(instance=note, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('notes')
    context = {'note': note, 'form': form}
    return render(request, 'edit_note.html', context)

# delete_note
def delete_note (request, note_id):
    note = Note.objects.get(id=note_id)
    note.delete()
    return redirect('notes')