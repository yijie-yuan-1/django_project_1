#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-10-05 22:38
# @Author  : Yijie Yuan
# @Site    : 
# @File    : urls.py
# @Software: PyCharm

from django.urls import path
from . import views

app_name = 'polls'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]

