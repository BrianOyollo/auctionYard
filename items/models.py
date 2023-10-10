from django.db import models
import uuid
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.utils.text import slugify

user = get_user_model()

# Create your models here.
class ItemCategory(models.Model):
    id = models.UUIDField(primary_key=True,default = uuid.uuid4, editable=False )
    category = models.CharField(max_length=150, blank=False, null=False, verbose_name='Category')
    description = models.TextField(max_length=250, verbose_name = 'Category description')

    class Meta:
        verbose_name_plural = 'Item Categories'

    def __str__(self):
        return self.category
    
reserve_status = (
    ('Reserve', "Reserve"), 
    ('No Reserve', 'No Reserve')
)

class ReserveStatus(models.Model):
    id = models.UUIDField(primary_key=True,default = uuid.uuid4, editable=False )
    status = models.CharField(max_length=150, blank=False, null=False, verbose_name='Status', choices=reserve_status)
    description = models.TextField(max_length=250, verbose_name = 'Status description')

    class Meta:
        verbose_name_plural = 'Reserve Status'

    def __str__(self):
        return self.status


item_status = (
    ('Available', 'Available'), 
    ('Sold', 'Sold'),
)

class ItemStatus(models.Model):
    id = models.UUIDField(primary_key=True,default = uuid.uuid4, editable=False )
    status = models.CharField(max_length=150, blank=False, null=False, verbose_name='Status', choices=item_status)
    description = models.TextField(max_length=250, verbose_name = 'Status description')

    class Meta:
        verbose_name_plural = 'Item Status'

    def __str__(self):
        return self.status


class Item(models.Model):
    id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    title = models.CharField(max_length=150, blank=False, null=False, verbose_name='Title')
    description = models.TextField( verbose_name = 'Item description', blank = False, null = False)
    item_category = models.ForeignKey(ItemCategory, on_delete=models.CASCADE, related_name='item_category')
    reserve_status = models.ForeignKey(ReserveStatus, on_delete=models.CASCADE, related_name='item_reserve_status')
    item_status = models.ForeignKey(ItemStatus, on_delete=models.CASCADE, related_name='item_status')
    reserve_price = models.FloatField(blank = True, null=True, default=0)
    cover_photo = models.ImageField(upload_to='cover_photos/', default='no_picture.jpg')
    seller = models.ForeignKey(user, on_delete=models.CASCADE, related_name='seller')
    date_posted = models.DateTimeField(auto_now_add=True, verbose_name='Date Posted')

    class Meta:
        verbose_name_plural = 'Items'

    def __str__(self):
        return self.title
    
class itemImages(models.Model):
    id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='image_item')
    image = models.ImageField(upload_to='item_images/')

    class Meta:
        verbose_name_plural = 'Item Images'

    def __str__(self):
        return str(self.id)
    
class Comment(models.Model):
    id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    user = models.ForeignKey(user, on_delete=models.CASCADE, related_name='user')
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='comment_item')
    comment = models.TextField(verbose_name='Comment')
    time = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        verbose_name_plural = 'Comments'

    def __str__(self):
        return f"{self.user} - {self.item}"

class Bid(models.Model):
    id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='bid_item')
    user = models.ForeignKey(user, on_delete=models.CASCADE, related_name='bidder')
    bid_amount = models.FloatField(blank=False, null=False, verbose_name="Bid Amount")
    bid_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Bids"

    def __str__(self):
        return f"{self.bid_time} - {self.item} - {self.bid_amount}"