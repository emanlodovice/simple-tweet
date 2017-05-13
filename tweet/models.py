# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Tweet(models.Model):
    owner = models.ForeignKey(User, related_name='tweets')
    content = models.CharField(max_length=255)
    when_created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return '{} by {}'.format(self.content, self.owner.username)
