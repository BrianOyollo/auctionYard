from django.shortcuts import render
from django.views.generic import ListView
from .models import Item, Bid, Comment
from django.shortcuts import get_list_or_404
from django.shortcuts import get_object_or_404
from django.db.models import Max

# Create your views here.
def HomePageView(request):
    items = Item.objects.annotate(max_bid = Max('bid_item__bid_amount')).order_by('-date_posted')

    context = {
        'items':items,
    }

    return render(request, 'homepage.html', context)

def ItemDetailView(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    bids = Bid.objects.filter(item=item)

    context = {
        'item':item,
        'bids':bids
    }

    return render(request, 'item_details.html', context)
