from django.urls import path
from .views import admin_login, admin_auth, save_ticket, complet_ticket, delete_ticket, terms, contact, about

urlpatterns = [
    path('', contact, name='contact'),
    path('about/', about, name='about'),
    path('terms-conditions/', terms, name='terms'),
    path('save-report/', save_ticket, name='support_save'),
]