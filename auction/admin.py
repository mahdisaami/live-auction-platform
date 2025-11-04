from django.contrib import admin

from auction.models import Bid, AuctionItem


@admin.register(Bid)
class BidAdmin(admin.ModelAdmin):
    list_display = ('item', 'amount', 'created_at')
    list_filter = ('item', 'created_at')
    search_fields = ('item__name',)

@admin.register(AuctionItem)
class AuctionItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'current_price', 'ends_at')
    search_fields = ('name',)