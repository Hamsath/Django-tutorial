# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from accounts.models import userProfile

# Register your models here.

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'user_info', 'city', 'website', 'phone']

    def user_info(self,obj):
        return obj.description

    def get_queryset(self,request):
        queryset = super(UserProfileAdmin,self).get_queryset(request)
        queryset = queryset.order_by('city')
        return queryset

admin.site.register(userProfile,UserProfileAdmin)
