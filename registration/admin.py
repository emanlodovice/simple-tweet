# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    search_fields = ['owner__username']


admin.site.register(UserProfile, UserProfileAdmin)
