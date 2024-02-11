from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Ticket
from .forms import TicketForm
from django.contrib.auth.models import User
from social.models import Post, Comment
# Create your views here.
# admin dash
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
    return render(request, 'terms.html')

# about
def about(request):
    return render(request, 'about.html')

def support_home(request):
    context = {
        'form': TicketForm()
    }
    return render(request, 'support.html', context)

def contact(request):
    context = {
        'form': TicketForm()
    }
    return render(request, 'contact.html', context)

def support_save(request):
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            form.save()
            form = TicketForm()
            context = {
                'form': form,
                'message': 'Tu reporte se ha creado correctamente, pronto nos pondremos en contacto contigo.'
            }
            return render(request, 'contact.html', context)
        else:
            context = {
                'form': form,
                'message': 'Los datos ingresados no son válidos'
            }
            return render(request, 'support.html', context)
    else:
        return support_home(request)
    

# complete tickets
def complet_ticket(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id)
    ticket.status = True
    ticket.save()
    return redirect('admin_dash', 'admin')

# delete tickets
def delete_ticket(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id)
    ticket.delete()
    return redirect('admin_dash', 'admin')