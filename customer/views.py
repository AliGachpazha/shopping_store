from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.db.models import F
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import FormView
from rest_framework.authtoken.models import Token

from order.models import Order, Cart, GiftCart
from .forms import UserForms, UserLogin, EditProfile, ChangePasswordForm, EmailForgot
from .models import User
import django.contrib.auth
from django.contrib.auth.decorators import user_passes_test

from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.views import generic
from rest_framework import viewsets, generics, status

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
                login(request, user)
                return redirect('product:home')
            messages.error(request, INVALID_USERNAME_PASSWORD)
            return redirect('customer:login')
        messages.error(request, form.errors.as_text())
        return redirect('customer:login')
    context = {
        'form': form,
    }
    return render(request, 'customer/login.html', context=context)


def edit_profile(request, user_id):
    std = get_object_or_404(User, id=user_id)
    form = EditProfile(instance=std)
    if request.method == 'POST':
        form = EditProfile(request.POST, instance=std)
        if form.is_valid() :
            form.save()
            return redirect('product:home')
    context = {
        'form': form,
        'std_id': std.id,
    }
    return render(request, 'customer/edit.html', context=context)


def profile(request, user_id):
    profile_user = User.objects.get(id=user_id)
    orders = Order.objects.filter(customer__id=user_id)
    try:
        gift_cart = GiftCart.objects.get(user__id=user_id)
        context = {'profile': profile_user, 'orders': orders, 'gift_cart': gift_cart}
        return render(request, 'customer/profile.html', context=context)
    except:
        context = {'profile': profile_user, 'orders': orders, }
        return render(request, 'customer/profile.html', context=context)


def list_users(request):
    list_user = User.objects.all()
    context = {'list_user': list_user}
    return render(request, 'customer/list_user.html', context=context)


def change_password_view(request, token):
    if request.method == 'POST':
        form = ChangePasswordForm(data=request.POST)
        context = {}
        try:
            user = Token.objects.get(key=token).user
            passwords = form.data
            if passwords['password1'] != passwords['password2']:
                context = {'error': 'password does not match'}
            else:
                user.set_password(passwords['password2'])
                user.save()
                return redirect(reverse('customer:login'))
        except Token.DoesNotExist:
            context = {'error': 'user does not exist'}
        return render(request, 'customer/email-password.html', context=context)
    form = ChangePasswordForm()
    context = {'form': form}
    return render(request, 'customer/email-password.html', context=context)


def forgot_password_view(request):
    if request.method == 'GET':
        form = EmailForgot()
        context = {'form': form}

        return render(request, 'customer/ForgotPassword.html', context=context)
    else:
        form = EmailForgot(data=request.POST)
        try:
            email = form.data.get('email')
            user = User.objects.get(email=email)
            context = {'status': 'change password link has been sent to your email'}
            # print(reverse('customer:change_password', args=[user.get_token()]))
            send_mail(
                'forgot password',
                'http://127.0.0.1:8000' + reverse_lazy('customer:change_password', args=[user.get_token()]),
                'online@gmail.com',
                [user.email],
                fail_silently=False
            )
        except User.DoesNotExist:
            context = {'status': 'user does not exist'}
            print('user does not exist')
        return render(request, 'customer/login.html', context=context)