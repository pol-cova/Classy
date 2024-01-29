from django.urls import path
from .views import support_home, support_save, support_tickets

urlpatterns = [
    path('', support_home, name='support_home'),
    path('save-report/', support_save, name='support_save'),
    path('all/tickets/', support_tickets, name='support_tickets')
]