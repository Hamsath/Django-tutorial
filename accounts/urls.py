from django.conf.urls import url
from . import views                     # using . will search in outer tutorial directory

urlpatterns=[
    url(r'^$',views.home),

]
