# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def home(request):
    myName='Hamsath'
    numbers=[1,2,3,4,5]

    args = {'myName':myName,'numbers':numbers}
    return render(request,'accounts/home.html',args)
