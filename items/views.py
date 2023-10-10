from django.shortcuts import render
from django.views.generic import ListView
from .models import Item, Bid, Comment, ItemStatus, itemImages
from django.shortcuts import get_list_or_404
from django.shortcuts import get_object_or_404
from django.db.models import Max
from .forms import AddItemForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

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
    item_images = itemImages.objects.filter(item=item).all()

    # forms
    # add_item_images_form = UploadFileForm(request.POST, request.FILES)

    context = {
        'item':item,
        'bids':bids,
        'max_bid':max_bid,
        'item_images':item_images
    }

    return render(request, 'item_details.html', context)

@login_required
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

            # get item_id
            new_item_id = add_item.id
            return redirect('item-details', new_item_id)
    else:
        add_item_form = AddItemForm(initial={'item_status':item_status})

    context = {
        'add_item_form':add_item_form,
    }

    return render(request, 'sell_item.html', context=context)


def addItemImagesView(request, item_id):
    item = Item.objects.get(id=item_id)

    if request.method == 'POST':
        images = request.FILES.getlist('images')
        for image in images:
            itemImages.objects.create(image=image,item=item)

        return redirect('item-details', item_id)
    
    context = {
        # 'add_item_images_form':add_item_images_form,
    }
    return render(request, 'sell_item.html', context=context)