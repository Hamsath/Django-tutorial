from django.conf.urls import url
from . import views                     # using . will search in outer tutorial directory
from django.contrib.auth.views import login

urlpatterns=[
    url(r'^$',views.home),
    url(r'^login/$',login,{'template_name':'accounts/login.html'})
]
