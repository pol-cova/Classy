from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import authenticate
from django.shortcuts import render, redirect, get_object_or_404
from .models import Ticket
from .forms import TicketForm
from django.contrib.auth.models import User
from social.models import Post, Comment
import os
# Mail settings
from django.core.mail import send_mail
from django.conf import settings

# admin login page
def admin_login(request):
    return render(request, 'admin_login.html')

# admin auth method
def admin_auth(request):
    if request.method == 'POST':
        mail = request.POST['mail']
        password = request.POST['password']
        SUPPORT_MAIL = os.getenv('SUPPORT_MAIL')
        SUPPORT_PASSWORD = os.getenv('SUPPORT_PASSWORD')
        user = authenticate(username=SUPPORT_MAIL, password=SUPPORT_PASSWORD)
        if user is not None:
            return 'Success'
        else:
            return 'Fail'
    else:
        return redirect('admin_login')

# admin dash
@login_required
def admin_dash(request, token):
    if token == 'admin':
        context = {
            'tickets': Ticket.objects.all(),
            'total_users': User.objects.all().count(),
            'total_posts': Post.objects.all().count(),
            'total_comments': Comment.objects.all().count(),
            'total_tickets': Ticket.objects.all().count(),
        }
        return render(request, 'support_admin.html', context)
    else:
        return redirect('home')

# terms and conditions
def terms(request):
    return render(request, 'conditions.html')

# about
def about(request):
    return render(request, 'about.html')

# contact
def contact(request):
    context = {
        'form': TicketForm()
    }
    return render(request, 'contact.html', context)

def save_ticket(request):
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            # user mail
            mail = form.cleaned_data['email']
            form.save()
            form = TicketForm()
            context = {
                'form': form,
                'message': 'Tu reporte se ha creado correctamente, pronto nos pondremos en contacto contigo.'
            }
            # send email
            subject = "noreply: Classy | Gracias por tu reporte"
            message = "Gracias por tu reporte, pronto nos pondremos en contacto contigo."
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [mail]
            send_mail(subject, message, email_from, recipient_list)

            return render(request, 'contact.html', context)
        else:
            context = {
                'form': form,
                'message': 'Los datos ingresados no son válidos'
            }
            return render(request, 'support.html', context)
    else:
        return contact(request)
    

# complete tickets
@login_required
def complet_ticket(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id)
    ticket.status = True
    ticket.save()
    return redirect('admin_dash', 'admin')

# delete tickets
@login_required
def delete_ticket(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id)
    ticket.delete()
    return redirect('admin_dash', 'admin')

def custom_404(request, exception):
    return render(request, '404.html', status=404)