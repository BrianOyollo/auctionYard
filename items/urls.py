from django.urls import path
from .views import (
    HomePageView,
    ItemDetailView,
    SellItemView,
    addItemImagesView
)

urlpatterns = [
    path('', HomePageView, name='homepage'),
    path('<uuid:item_id>/', ItemDetailView, name='item-details'),
    path('sell-item/', SellItemView, name='sell-item'),
    path('<uuid:item_id>/add-item-images/', addItemImagesView, name='add-item-images'),
]