from django.urls import path
from . import views

urlpatterns = [
    path("", views.notes, name="notes"),
    path("add_note/", views.add_note, name="add_note"),
]