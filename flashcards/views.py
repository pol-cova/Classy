from django.shortcuts import render, redirect
from .forms import CardGroupForm, CardForm
from .models import CardGroup, Card
from django.contrib.auth.decorators import login_required
# Renders  
@login_required(login_url='/login')
def index(request):
    # get users card groups
    card_groups = CardGroup.objects.filter(user=request.user)
    context = {
        'new_card_group_form': CardGroupForm(),
        'card_groups': card_groups
    }
    return render(request, 'flash.html', context)

@login_required(login_url='/login')
# Flash cards view
def flash_cards(request, card_group_id):
    # get card group
    card_group = CardGroup.objects.get(id=card_group_id)
    # get cards from card group
    cards = Card.objects.filter(card_group=card_group)
    context = {
        'card_group': card_group,
        'cards': cards,
        'new_card_form': CardForm()
    }
    return render(request, 'flash-cards.html', context)

# Logic section
# Create a new card group
@login_required(login_url='/login')
def create_card_group(request):
    if request.method == 'POST':
        form = CardGroupForm(request.POST)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
    return redirect('flash')

@login_required(login_url='/login')
def create_card(request, card_group_id):
    if request.method == 'POST':
        form = CardForm(request.POST)
        if form.is_valid():
            form.instance.card_group = CardGroup.objects.get(id=card_group_id)
            # add user
            form.instance.user = request.user
            form.save()
    return redirect('flash-cards', card_group_id=card_group_id)

# Delete all cards in a card group
@login_required(login_url='/login')
def delete_cards(request, card_group_id):
    Card.objects.filter(card_group=card_group_id).delete()
    return redirect('flash-cards', card_group_id=card_group_id)