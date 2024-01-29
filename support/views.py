from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required
from .models import Ticket
from .forms import TicketForm


# Create your views here.

def support_home(request):
    contex = {
        'form': TicketForm()
    }
    return render(request, 'support.html', contex)

def support_save(request):
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            form.save()
            form = TicketForm()
            contex = {
                'form': form,
                'message': 'Tu reporte se ha creado correctamente, pronto nos pondremos en contacto contigo.'
            }
            return render(request, 'support.html', contex)
        else:
            contex = {
                'form': form,
                'message': 'Los datos ingresados no son válidos'
            }
            return render(request, 'support.html', contex)
    else:
        return support_home(request)
    
@login_required
def support_tickets(request):
    tickets = Ticket.objects.all()
    context = {
        'tickets': tickets
    }
    return render(request, 'support_tickets.html', context)