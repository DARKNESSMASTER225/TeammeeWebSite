import datetime

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm

from rest_framework.permissions import IsAuthenticated
from .models import Profile
from .serializers import ProfileSerializer

from rest_framework.response import Response
from django.middleware import csrf
from django.middleware import csrf
from rest_framework.schemas import DefaultSchema

from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Ваш аккаунт создан: можно войти на сайт.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


def main(request):
    return render(request, 'main.html')


def handle_payment(request):
    tariff_id = request.GET.get('tariff_id')
    user = request.user
    user.profile.tarif_level = tariff_id
    if int(tariff_id) in [1, 2, 3, 4]:
        user.profile.tariff_exp = datetime.date.today() + datetime.timedelta(days=30)
    elif int(tariff_id) in [5, 6, 7, 8]:
        user.profile.tariff_exp = datetime.date.today() + datetime.timedelta(days=365)
    user.save()

    return render(request, 'payment_handle.html')


def checkout(request):
    tariff = request.GET.get('tariff')
    tariff_id = request.GET.get('id')
    payment_amount = request.GET.get('payment_amount')

    return render(request, 'tariff_checkout.html', {'tariff': tariff, 'tariff_id': tariff_id, 'payment_amount': payment_amount})


def tarifs(request):
    return render(request, 'tarifs.html')


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Ваш профиль успешно обновлен.')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'users/profile.html', context)
