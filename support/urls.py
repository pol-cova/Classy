from django.urls import path
from .views import support_home, support_save, complet_ticket, delete_ticket, terms, contact, about, admin_dash

urlpatterns = [
    path('', support_home, name='support_home'),
    path('dash/<str:token>/', admin_dash, name='admin_dash'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('terms-conditions/', terms, name='terms'),
    path('save-report/', support_save, name='support_save'),
    path('complete/ticket/<int:ticket_id>/', complet_ticket, name='complet_ticket'),
    path('delete/ticket/<int:ticket_id>/', delete_ticket, name='delete_ticket'),
]