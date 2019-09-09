# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Tweets(models.Model):
    time_stamp = models.DateTimeField('date published')
    twitter_id = models.IntegerField(default=0)
    python_tip = models.CharField(max_length=280)
    who_posted = models.CharField(max_length=50)

    def __str__(self):
        return self.python_tip
