from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import StoreItem
from logins.models import Player

@login_required
def redeem_item(request, item_id):
    item = StoreItem.objects.get(pk=item_id)
    player = request.user.player

    if player.points >= item.cost:
        player.points -= item.cost
        player.save()
        player.purchased_items.add(item)
        request.user.profile_pic = item.image
        request.user.save()
        messages.success(request, f'Redeemed {item.name} successfully!')
    else:
        messages.error(request, f'Not enough points to redeem {item.name}.')

    return redirect('store')


def store(request):
    print("Store view called")
    items = StoreItem.objects.all()
    print(items)
    context = {'items': items}
    return render(request, 'store.html', context)
