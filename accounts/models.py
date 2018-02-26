# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class userProfile(models.Model):
    user=models.OneToOneField(User)
    description=models.CharField(max_length=100,default='')
    city=models.CharField(max_length=20,default='')
    website=models.URLField(default='')
    phone=models.IntegerField(default=0)
