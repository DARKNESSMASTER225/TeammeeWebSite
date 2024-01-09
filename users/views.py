import datetime

from django.db import transaction
from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm

from rest_framework.permissions import IsAuthenticated
from .models import Profile, Group
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
    return render(request, 'register.html', {'form': form})


def main(request):
    return render(request, 'main.html')


def handle_payment(request):
    tariff_id = request.GET.get('tariff_id')
    tariff_exp = request.GET.get('tariff_exp')
    volume = request.GET.get('volume')
    tariff_exp_date = datetime.date.today() + datetime.timedelta(days=int(tariff_exp) * 30)
    user = request.user
    try:
        with transaction.atomic():
            group = Group(
                tariff_level=tariff_id,
                tariff_exp=tariff_exp_date,
                volume=volume,
                owner=user
            )
            group.save()
            user.group = group
            user.save()
            group.members.add(user)
            group.save()
            return render(request, 'payment_handle.html')
    except Exception:
        return HttpResponseNotFound()


def checkout(request):
    tariff = request.GET.get('tariff')
    tariff_id = request.GET.get('tariff_id')
    payment_amount = request.GET.get('payment_amount')
    tariff_exp = request.GET.get('tariff_exp')
    volume = request.GET.get('volume')
    return render(request, 'tariff_checkout.html',
                  {'volume': volume, 'tariff': tariff, 'tariff_exp': tariff_exp, 'tariff_id': tariff_id,
                   'payment_amount': payment_amount})


def tariffs(request):
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

    return render(request, 'profile.html', context)
