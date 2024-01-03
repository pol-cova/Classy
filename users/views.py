from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

# index 
def index(request):
    # check if request user is auth
    if request.user.is_authenticated:
        return Response({'message': 'Hello, ' + request.user.username})
    else:
        return render(request, 'index.html')