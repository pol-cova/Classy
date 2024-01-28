from django.urls import path
from . import views

urlpatterns = [
    path('', views.social_home, name='social_home'),
]