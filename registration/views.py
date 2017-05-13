# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse

from forms import UserInfoForm


def sign_in(request):
    if request.user.is_authenticated:
        return redirect('/')
    context = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            print user.get_full_name()
            if user.get_full_name() == '':
                return redirect(reverse('edit_profile'))
            return redirect('/')
        else:
            context['error'] = 'Invalid Username of Password'
            context['username'] = username
    return render(request, 'registration/sign_in.html', context=context)


def sign_up(request):
    if request.user.is_authenticated:
        return redirect('/')
    context = {}
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            context['success'] = True
    else:
        form = UserCreationForm()
    context['form'] = form
    return render(request, 'registration/sign_up.html', context=context)


def edit_profile(request):
    if not request.user.is_authenticated:
        return redirect('sign_in')

    if request.method == 'POST':
        form = UserInfoForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect(
                reverse('profile', kwargs={'username': request.user.username}))
    else:
        form = UserInfoForm(instance=request.user)
    context = {
        'form': form
    }
    return render(request, 'registration/edit_profile.html', context=context)


def sign_out(request):
    logout(request)
    return redirect('sign_in')
