from django.shortcuts import render, redirect
from .forms import CardGroupForm, CardForm
from .models import CardGroup, Card
from django.contrib.auth.decorators import login_required
# Renders  
@login_required
def index(request):
    # get users card groups
    card_groups = CardGroup.objects.filter(user=request.user)
    context = {
        'new_card_group_form': CardGroupForm(),
        'card_groups': card_groups
    }
    return render(request, 'flash.html', context)

@login_required
# Flash cards view
def flash_cards(request, card_group_id):
    # get card group
    card_group = CardGroup.objects.get(id=card_group_id)
    # get cards from card group
    cards = Card.objects.filter(card_group=card_group)
    context = {
        'card_group': card_group,
        'cards': cards,
    }
    return render(request, 'flash-cards.html', context)

# Logic section
# Create a new card group
@login_required
def create_card_group(request):
    if request.method == 'POST':
        form = CardGroupForm(request.POST)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
    return redirect('flash')

