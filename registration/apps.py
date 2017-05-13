# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.apps import AppConfig


class RegistrationConfig(AppConfig):
    name = 'registration'

    def ready(self):
        """ activate signals """
        from registration import signals
