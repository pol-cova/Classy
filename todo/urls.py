from django.urls import path
from . import views

urlpatterns = [
    path('', views.todo, name='todo'),
    path('add_task/', views.add_task, name='add_task'),
    path('new_task/', views.new_task, name='new_task'),
    path('add_group/', views.add_group, name='add_group'),
    path('edit_task/<int:task_id>/', views.edit_task, name='edit_task'),
    path('delete_task/<int:task_id>/', views.delete_task, name='delete_task'),
    path('complete_task/<int:task_id>/', views.complete_task, name='complete_task'),
    path('incomplete_task/<int:task_id>/', views.decomplete_task, name='incomplete_task'),
    path('filter_group/<int:group_id>/', views.filter_group, name='filter_group')
]