#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
Urls for the website app.
"""
__author__ = 'David Bonnet/Wintercap'

from django.conf.urls import url, patterns

urlpatterns = patterns('website.views',
    url(r'^$', 'home'),
)