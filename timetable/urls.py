from django.urls import path
from . import views

urlpatterns = [
    path('', views.timetable, name='timetable'),
    path('add_subject/', views.add_subject, name='add_subject'),
    path('delete_subject/<int:pk>/', views.delete_subject, name='delete_subject'),
]