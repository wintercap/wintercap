#-*- coding: utf-8 -*-
"""
wintercap.fr website views
"""
from __future__ import print_function, division, absolute_import, unicode_literals
from collections import OrderedDict

from django.shortcuts import render


def make_nav(active_page):
    """
    This function builds the navbar as an orderd dict.
    Each page name is a key, its value is the destination view.
    """
    pages = (
        'Accueil',
        'Compétences',
        'Réalisations',
        'Contact',
    )
    views = (
        'website.views.home',
        'website.views.home',
        'website.views.home',
        'website.views.home',
    )
    nav_pages = OrderedDict(zip(pages, views))
    return nav_pages


def home(request):
    """
    Home page.
    """
    page_title = 'Accueil'
    nav_pages = make_nav(page_title)

    return render(request, 'website/home.html', locals())