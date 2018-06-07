#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : urls.py
# @Author: huyn
# @Date  : 2018/6/6
# @Desc  :

#
# from django.conf.urls import url,include
# from sign import views
# from django.contrib import admin
#
#
#
# urlpatterns = [
#     url(r'^admin/', admin.site.urls),
#     url(r'^index/$', views.index),
#     url(r'^logout/$', views.logout),
#     url(r'^accounts/login/$', views.index),
#     url(r'^login_action/$', views.login_action),
#     url(r'^event_manage/$', views.event_manage),
#     url(r'^guest_manage/$', views.guest_manage),
#     url(r'^search_name/$', views.search_name),
#     url(r'^search_guest/$', views.search_guest),
#     url(r'^sign_index/(?P<eid>[0-9])+/$',views.sign_index),
#     url(r'^sign_index_action/(?P<eid>[0-9])+/$',views.sign_index_action),
#     url(r'^api/',include('sign.urls',namespace='sign')),
# ]
from django.conf.urls import url
from django.contrib import admin
from sign import views_if,views_if_sec

urlpatterns = [
    url(r'^add_event/', views_if.add_event,name='add_event'),
    url(r'^add_guest/', views_if.add_guest,name='add_guest'),
    url(r'^get_event_list/', views_if.get_event_list,name='get_event_list'),
    url(r'^get_guest_list/', views_if.get_guest_list,name='get_guest_list'),
    url(r'^user_sign/', views_if.user_sign,name='user_sign'),
    url(r'^sec_get_event_list/', views_if_sec.sec_get_event_list, name='sec_get_event_list'),
    url(r'^sec_add_event/', views_if_sec.sec_add_event,name='sec_add_event'),
]