from django.contrib import admin
from .models import (
    ItemCategory,
    ItemStatus,
    ReserveStatus,
    Item, 
    Comment,
    Bid,
    itemImages
)

# Register your models here.
admin.site.register(ItemCategory)
admin.site.register(ItemStatus)
admin.site.register(ReserveStatus)
admin.site.register(Item)
admin.site.register(Comment)
admin.site.register(Bid)
admin.site.register(itemImages)