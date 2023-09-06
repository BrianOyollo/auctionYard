from django.urls import path
from .views import(
    TestPageView,
    user_profile_view,
)
from django.contrib.auth.views import(
    PasswordResetView,
    PasswordResetView, 
    PasswordResetDoneView, 
    PasswordResetConfirmView,
    PasswordResetCompleteView,
)

urlpatterns = [
    path('', TestPageView.as_view(), name='homepage'),
    path('profile/', user_profile_view, name = 'user-profile'),
    path('password-reset/', PasswordResetView.as_view(template_name='account/password_reset.html'), name = 'password_reset'),
    path('password-reset/done/', PasswordResetView.as_view(template_name='account/password_reset_done.html'), name = 'password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='account/password_reset_confirm.html'),name='password_reset_confirm'),
    path('password-reset-complete/',PasswordResetCompleteView.as_view(template_name='account/password_reset_complete.html'),name='password_reset_complete'),
]