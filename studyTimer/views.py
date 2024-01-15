from django.shortcuts import render

# Create your views here.
def studyTimer(request):
    return render(request, 'timer.html')