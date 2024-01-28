from django.shortcuts import render
from django.utils import timezone
from .models import Post, Comment
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

# home social page
@login_required
def social_home(request):
    return render(request, 'social.html')