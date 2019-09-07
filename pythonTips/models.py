# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Tweets(models.Model):
    time_stamp = models.DateTimeField('date published')
    python_tip = models.CharField(max_length=280)
    twitter_id = models.CharField(max_length=50)
