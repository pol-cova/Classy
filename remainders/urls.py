from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='remainders'),
    path('create/', views.create_remainder, name='create_remainder'),
    path('delete/<int:remainder_id>/', views.delete_remainder, name='delete_remainder'),
    path('update/<int:remainder_id>/', views.update_remainder, name='update_remainder'),
    path('complete/<int:remainder_id>/', views.complete_remainder, name='complete_remainder'),
    path('uncomplete/<int:remainder_id>/', views.uncomplete_remainder, name='uncomplete_remainder'),
    
]