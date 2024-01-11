from django.urls import path
from . import views

urlpatterns = [
    path('', views.todo, name='todo'),
    path('add_task/', views.add_task, name='add_task'),
]