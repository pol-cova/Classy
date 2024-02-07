from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='flash'),
    path('create-card-group/', views.create_card_group, name='create-card-group'),
    path('group/<int:card_group_id>/', views.flash_cards, name='flash-cards'),
    path('create-card/<int:card_group_id>/', views.create_card, name='create-card'),
]