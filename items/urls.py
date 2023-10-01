from django.urls import path
from .views import (
    HomePageView,
    ItemDetailView,
    SellItemView,
)

urlpatterns = [
    path('', HomePageView, name='homepage'),
    path('<uuid:item_id>/', ItemDetailView, name='item-details'),
    path('sell-item/', SellItemView, name='sell-item'),
]