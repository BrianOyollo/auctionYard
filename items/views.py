from django.shortcuts import render
from django.views.generic import ListView
from .models import Item

# Create your views here.
class HomePageView(ListView):
    model = Item
    context_object_name = 'items'
    template_name = 'homepage.html'