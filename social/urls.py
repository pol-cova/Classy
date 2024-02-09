from django.urls import path
from . import views

urlpatterns = [
    path('', views.social_home, name='social_home'),
    path('create_post/', views.create_post, name='create_post'),
    path('like_post/<int:post_id>/', views.like_post, name='like_post'),
    path('dislike_post/<int:post_id>/', views.dislike_post, name='dislike_post'),
    path('create_comment/<int:post_id>/', views.create_comment, name='create_comment'),
    path('like_comment/<int:comment_id>/', views.like_comment, name='like_comment'),
    path('dislike_comment/<int:comment_id>/', views.dislike_comment, name='dislike_comment'),
    path('details/<int:post_id>/', views.post_detail, name='details'),
]