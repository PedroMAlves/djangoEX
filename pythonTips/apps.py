# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.apps import AppConfig


class PythontipsConfig(AppConfig):
    name = 'pythonTips'

    def ready(self):
        from scheduler import updater
        updater.start()