from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Bin, BinItemThrough
from django.core.exceptions import ObjectDoesNotExist
from logins.models import Player
from event.models import Trash


@login_required
def player_inventory(request):
    """
    View function to display the player's inventory of collected trash.

    Args:
        request (HttpRequest): The request object.

    Returns:
        HttpResponse: Rendered template with the player's inventory, total bin value, and points.
    """
    # Get the player object associated with the logged-in user
    player = Player.objects.get(user=request.user)

    # Retrieve the player's bin or create a new one if it doesn't exist
    try:
        player_bin = Bin.objects.get(player=player)
    except ObjectDoesNotExist:
        new_bin = Bin.objects.create(player=player)
        new_bin.save()
        player_bin = new_bin

    # Get the inventory of trash items in the player's bin
    inventory = BinItemThrough.objects.filter(bin=player_bin)

    # Calculate the total value of the trash items and player's points
    total_bin_value = player_bin.total_bin_value()
    points = player.points

    context = {
        'inventory': inventory,
        'total_bin_value': total_bin_value,
        'points': points,
    }

    return render(request, 'bin/player_bin.html', context)


@login_required
def trash_detail(request, trash_id):
    """
    View function to display the details of a trash item.

    Args:
        request (HttpRequest): The request object.
        trash_id (int): The ID of the trash item to display.

    Returns:
        HttpResponse: Rendered template with the trash item details and its presence in the player's bin.
    """
    # Get the trash item by its ID
    trash = Trash.objects.get(pk=trash_id)

    # Get the player object associated with the logged-in user
    player = Player.objects.get(user=request.user)

    # Get the player's bin
    player_bin = Bin.objects.get(player=player)

    # Check if the trash item is in the player's bin
    try:
        bin_item = BinItemThrough.objects.get(bin=player_bin, trash=trash)
    except BinItemThrough.DoesNotExist:
        bin_item = None

    context = {
        'trash': trash,
        'bin_item': bin_item,
    }

    return render(request, 'bin/trash_lookup.html', context)