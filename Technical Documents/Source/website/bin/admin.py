from django.contrib import admin
from .models import Bin, BinItemThrough

@admin.register(Bin)
class BinAdmin(admin.ModelAdmin):
    """
    BinAdmin class to display the player's bin and its content in the admin panel.
    """

    list_display = ('player', 'total_bin_value')
    search_fields = ('player__user__username',)

    def get_queryset(self, request):
        """
        Override the default queryset to include the related player and inventory items.
        """
        queryset = super().get_queryset(request)
        queryset = queryset.select_related('player__user').prefetch_related('inventory')
        return queryset

@admin.register(BinItemThrough)
class BinItemThroughAdmin(admin.ModelAdmin):
    """
    BinItemThroughAdmin class to display the trash items in the player's bin in the admin panel.
    """

    list_display = ('bin', 'trash', 'amount', 'total_value')
    search_fields = ('bin__player__user__username', 'trash__name')
    list_filter = ('trash',)