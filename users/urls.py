from django.urls import path
from .views import(
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
    path('user/profile/', user_profile_view, name = 'user-profile'),
    path('user/password-reset/', PasswordResetView.as_view(template_name='account/password_reset.html'), name = 'password_reset'),
    path('user/password-reset/done/', PasswordResetDoneView.as_view(template_name='account/password_reset_done.html'), name = 'password_reset_done'),
    path('user/password-reset-confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='account/password_reset_confirm.html'),name='password_reset_confirm'),
    path('user/password-reset-complete/',PasswordResetCompleteView.as_view(template_name='account/password_reset_complete.html'),name='password_reset_complete'),
]