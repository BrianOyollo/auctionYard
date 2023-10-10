from django import forms
from .models import *


class AddItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['title','description','item_category','reserve_status','reserve_price','cover_photo']
        widgets= {
            'description':forms.Textarea(attrs={'rows':2}),
            'reserve_status': forms.RadioSelect(),
        }
