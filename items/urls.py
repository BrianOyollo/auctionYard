from django.urls import path
from .views import (
    HomePageView,
    ItemDetailView
)

urlpatterns = [
    path('', HomePageView, name='homepage'),
    path('<uuid:item_id>/', ItemDetailView, name='item-details'),
]