from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .forms import UpdateUserForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import logging

# Create your views here.
@login_required()
def user_profile_view(request):
    update_form = UpdateUserForm(instance=request.user)
    password_change_form = PasswordChangeForm(request.user)

    if request.method == "POST":

        # profile update
        if "update_profile" in request.POST:
            update_form = UpdateUserForm(request.POST,instance=request.user)
            if update_form.is_valid():
                update_form.save()
                messages.success(request, "Profile updated successfully!")
                return redirect('user-profile')
            else:
                messages.error(request, 'Please fix the errors!')

        # password change
        if "update_password" in request.POST:
            password_change_form = PasswordChangeForm(request.user, request.POST)
            if password_change_form.is_valid():
                user = password_change_form.save() 
                update_session_auth_hash(request, user)
                messages.success(request, "Password changed successfully!")
            else:
                messages.error(request, "Please correct the errors below!")

    else:
        update_form = UpdateUserForm(instance=request.user)
        password_change_form = PasswordChangeForm(request.user)
        

    context = {
        "update_form":update_form,
        "password_change_form":password_change_form
    }

    return render(request, 'users/profile.html', context)