# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("<H1>Hello world. This is my best atempt</H1>")