from django.shortcuts import render
from django.utils import timezone
from .models import Post, Comment
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .forms import PostForm, CommentForm
from django.db.models import Count
# home social page
@login_required(login_url='/login')
def social_home(request):
    posts = Post.objects.annotate(comment_count=Count('comment')).order_by('-created')
    # get comments for each post
    for post in posts:
        post.comments = Comment.objects.filter(post=post).order_by('-created')
    
    context = {
        'new_post_form': PostForm(),
        'comment_form': CommentForm(),
        'posts': posts,
    }
    return render(request, 'social.html', context)

# create post
@login_required(login_url='/login')
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            # create post object but don't save to database yet
            post = form.save(commit=False)
            # assign the current logged in user to the post
            post.user = request.user
            # save post to database
            post.save()
            return redirect('social_home')
    else:
        form = PostForm()
    return redirect('social_home')

# like post
@login_required(login_url='/login')
def like_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.user in post.likes.all() or request.user in post.dislikes.all():
        post.likes.remove(request.user)
        post.dislikes.remove(request.user)
    else:
        post.likes.add(request.user)
    return redirect('social_home')

# dislike post
@login_required(login_url='/login')
def dislike_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.user in post.likes.all():
        post.likes.remove(request.user)
    else:
        post.dislikes.add(request.user)
    return redirect('social_home')

# create comment
@login_required(login_url='/login')
def create_comment(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            # create comment object but don't save to database yet
            comment = form.save(commit=False)
            # assign the current logged in user to the comment
            comment.user = request.user
            # assign the post to the comment
            comment.post = post
            # save comment to database
            comment.save()
            return redirect('details', post_id=comment.post.id)
    else:
        form = CommentForm()
    return redirect('details', post_id=comment.post.id)

# like comment
@login_required(login_url='/login')
def like_comment(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.user in comment.likes.all() or request.user in comment.dislikes.all():
        comment.likes.remove(request.user)
        comment.dislikes.remove(request.user)
    else:
        comment.likes.add(request.user)
    return redirect('details', post_id=comment.post.id)

# dislike comment
@login_required(login_url='/login')
def dislike_comment(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.user in comment.likes.all():
        comment.likes.remove(request.user)
    else:
        comment.dislikes.add(request.user)
    return redirect('details', post_id=comment.post.id)

# post detail
@login_required(login_url='/login')
def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    comments = Comment.objects.filter(post=post).order_by('-created')
    context = {
        'post': post,
        'comments': comments,
        'comment_form': CommentForm()
    }
    return render(request, 'post-detail.html', context)