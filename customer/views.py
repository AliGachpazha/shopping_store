from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.urls import reverse
from django.views import generic
from django.db.models import F
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect

from order.models import Order, Cart
from .forms import UserForms, UserLogin, EditProfile
from .models import User
import django.contrib.auth
from django.contrib.auth.decorators import user_passes_test

from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.views import generic
from rest_framework import viewsets, generics

from .models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import Group
from django.contrib import messages
from .vars import *
from django.contrib.auth.views import LogoutView


# Create your views here.
def register_form(request):
    user_forms = UserForms()
    return render(request, 'customer/register.html', context={
        'user_forms': user_forms
    })


def user_login(request):
    form = UserLogin()
    if request.method == 'POST':
        form = UserLogin(request.POST)
        if form.is_valid():
            user = authenticate(username=form.data['username'], password=form.data['password'])
            if user:
                if user.user_type == form.data['user_type']:
                    login(request, user)
                    return redirect('product:home')
                messages.error(request, INVALID_LEVEL)
                return redirect('customer:login')
            messages.error(request, INVALID_USERNAME_PASSWORD)
            return redirect('customer:login')
        messages.error(request, form.errors.as_text())
        return redirect('customer:login')
    context = {
        'form': form,
    }
    return render(request, 'customer/login.html', context=context)


# def view_profile(request):
#     args = {'user': request.user}
#     return render(request, 'customer/view.html', context=args)


def edit_profile(request, user_id):
    std = get_object_or_404(User, id=user_id)
    form = EditProfile(instance=std)
    if request.method == 'POST':
        form = EditProfile(request.POST, instance=std)
        if form.is_valid():
            user = form.save()
            if form.cleaned_data['new_password'] == form.cleaned_data['new_passwordconfirm']:
                user.set_password(form.cleaned_data['new_password'])
                user.save()
                login(request, user)
            else:
                messages.error(request, "PASSWORD INCORRECT")
                return redirect('customer:edit')
            return redirect('product:home')
    context = {
        'form': form,
        'std_id': std.id,
    }
    return render(request, 'customer/edit.html', context=context)


def profile(request, user_id):
    # context = super().get_context_data(**kwargs)
    profile_user = User.objects.get(id=user_id)
    orders = Order.objects.filter(customer__id =user_id)
    context = {'profile': profile_user,'orders':orders }
    return render(request, 'customer/profile.html', context=context)


def list_users(request):
    list_user = User.objects.all()
    context = {'list_user': list_user}
    return render(request, 'customer/list_user.html', context=context)
