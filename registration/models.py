# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.contrib.staticfiles.templatetags.staticfiles import static


def avatar_upload_path(instance, filename):
    return './storage/user_{}_{}'.format(instance.owner.username, filename)


class UserProfile(models.Model):
    owner = models.OneToOneField(User, related_name='profile')
    avatar = models.FileField(upload_to=avatar_upload_path, blank=True)

    @property
    def avatar_url(self):
        if self.avatar:
            return self.avatar.url
        return static('img/default_avatar.png')

    def __unicode__(self):
        return self.owner.username
