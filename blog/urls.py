# -*- coding: utf-8 -*-
"""
Created on Fri Aug  4 13:36:38 2017

@author: yuriy
"""

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
]

