from django.urls import path
from .views import(
    TestPageView,
    user_profile_view,
)

urlpatterns = [
    path('', TestPageView.as_view(), name='homepage'),
    path('profile/', user_profile_view, name = 'user-profile'),
]