# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from home.forms import HomeForm
from home.models import Post,Friend


# Create your views here.

class HomeView(TemplateView):
    template_name = 'home/home.html'

    def get(self, request):
        form = HomeForm()
        posts = Post.objects.all().order_by('-created')
        users = User.objects.exclude(id=request.user.id)
        friend,created = Friend.objects.get_or_create(current_user=request.user)
        friends = friend.users.all()
        current_user_posts = Post.objects.filter(user_id=request.user.id)

        args = {'form':form, 'posts': posts, 'users':users,'friends':friends,'current_user_posts':current_user_posts}

        return render(request,self.template_name,args)

    def post(self, request):
        form = HomeForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            text = form.cleaned_data['post']
            form = HomeForm()
            return redirect('home:home')

        args = {'form':form , 'text':text }
        return render(request,self.template_name,args)

def change_friends(request, operation , pk):
    friend = User.objects.get(pk=pk)
    if operation == 'add':
        Friend.make_friend(request.user,friend)
    elif operation == 'remove':
        Friend.lose_friend(request.user,friend)

    if (request.META['HTTP_REFERER'] == 'http://127.0.0.1:8000/home/friends/'):
        return redirect('home:friends')

    return redirect('home:home')


def delete_post(request,post_id):
    if post_id:
        user_post = Post.objects.filter(id=post_id)
        Post.delete_post_data(request,user_post)

    return redirect('home:home')

def friends(request):
    friend,created = Friend.objects.get_or_create(current_user=request.user)
    friends = friend.users.all()

    args = {'friends':friends}

    return render(request, 'home/friends.html',args)
