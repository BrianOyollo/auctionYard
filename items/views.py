from django.shortcuts import render
from django.views.generic import ListView
from .models import Item, Bid, Comment, ItemStatus
from django.shortcuts import get_list_or_404
from django.shortcuts import get_object_or_404
from django.db.models import Max
from .forms import AddItemForm
from django.shortcuts import redirect

# Create your views here.
def HomePageView(request):
    items = Item.objects.annotate(max_bid = Max('bid_item__bid_amount')).order_by('-date_posted')

    context = {
        'items':items,
    }

    return render(request, 'homepage.html', context)

def ItemDetailView(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    bids = Bid.objects.filter(item=item).all()
    max_bid = Bid.objects.filter(item=item).aggregate(max_bid_amount=Max('bid_amount'))

    context = {
        'item':item,
        'bids':bids,
        'max_bid':max_bid
    }

    return render(request, 'item_details.html', context)

def SellItemView(request):
    seller = request.user
    item_status = ItemStatus.objects.filter(status='Available').first()

    if request.method == 'POST':
        add_item_form = AddItemForm(request.POST, request.FILES)
        if add_item_form.is_valid():
            add_item = add_item_form.save(commit=False)
            add_item.seller = seller
            add_item.item_status = item_status
            add_item.save()
            return redirect('homepage')
    else:
        add_item_form = AddItemForm(initial={'item_status':item_status})
    
    context = {
        'form':add_item_form
    }

    return render(request, 'sell_item.html', context=context)