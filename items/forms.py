from django import forms
from .models import *


class AddItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['title','description','item_category','reserve_status','reserve_price','cover_photo']

class AddItemImages(forms.ModelForm):
    class Meta:
        model = itemImages
        fields = ['image']
        widgets = {
            'image': forms.ClearableFileInput(attrs={'allow_multiple_selected': True}),
        }