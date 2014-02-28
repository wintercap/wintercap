#-*- coding: utf-8 -*-
"""
Urls for the website app.
"""
from __future__ import print_function, division
from __future__ import absolute_import, unicode_literals
__author__ = 'David Bonnet/Wintercap'

from django.conf.urls import url, patterns

urlpatterns = patterns('website.views',
    url(r'^$', 'home'),
    url(r'^competences/$', 'competences'),
    url(r'^realisations/$', 'realisations'),
    url(r'^contact/$', 'contact'),
)