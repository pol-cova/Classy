from django.urls import path
from .views import admin_login, admin_auth, save_ticket, complet_ticket, delete_ticket, terms, contact, about

urlpatterns = [
    path('', contact, name='contact'),
    path('admin/', admin_login, name='admin_login'),
    path('admin/auth/', admin_auth, name='admin_auth'),
    path('about/', about, name='about'),
    path('terms-conditions/', terms, name='terms'),
    path('save-report/', save_ticket, name='support_save'),
    path('complete/ticket/<int:ticket_id>/', complet_ticket, name='complet_ticket'),
    path('delete/ticket/<int:ticket_id>/', delete_ticket, name='delete_ticket'),
]