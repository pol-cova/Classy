from django.shortcuts import render
from django.utils import timezone
from .models import Post, Comment
from .forms import PostForm, CommentForm
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('created')
    
