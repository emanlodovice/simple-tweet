# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import redirect
from django.urls import reverse

from .models import Tweet


def add_tweet(request):
    if not request.user.is_authenticated:
        return redirect(reverse('sign_in'))
    redirect_url = request.GET.get('next')
    if redirect_url is None:
        redirect_url = '/'
    if request.method == "POST":
        content = request.POST.get('content')
        Tweet.objects.create(content=content, owner=request.user)
    return redirect(redirect_url)
