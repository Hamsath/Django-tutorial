# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.

class UserProfileManager(models.Manager):
    def get_queryset(self):
        return super(UserProfileManager,self).get_queryset()   # use .filter(website='www.google.com') to filter the rows accordingly

class userProfile(models.Model):
    user=models.OneToOneField(User)
    description=models.CharField(max_length=100,default='')
    city=models.CharField(max_length=20,default='')
    website=models.URLField(default='')
    phone=models.IntegerField(default=0)
    image = models.ImageField(upload_to='profile_image',blank=True)
    objects = models.Manager()

    chennai = UserProfileManager()

    def __str__(self):
        return self.user.username

def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = userProfile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile,sender=User)    # signals are used to execute some code after a certain action
