from django.urls import path
from .views import TestPageView

urlpatterns = [
    path('', TestPageView.as_view(), name='homepage'),
]