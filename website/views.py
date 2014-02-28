#-*- coding: utf-8 -*-
"""
wintercap.fr website views
"""
from __future__ import print_function, division
from __future__ import absolute_import, unicode_literals
from collections import OrderedDict

from django.shortcuts import render

from website.models import *

def make_nav(active_page):
    """
    This function builds the navbar as an ordered dict.
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
        'website.views.competences',
        'website.views.realisations',
        'website.views.contact',
    )
    nav_pages = OrderedDict(zip(pages, views))
    return nav_pages


def home(request):
    page_title = 'Accueil'
    nav_pages = make_nav(page_title)

    return render(request, 'website/home.html', locals())


def competences(request):
    page_title = 'Compétences'
    nav_pages = make_nav(page_title)

    return render(request, 'website/competences.html', locals())


def realisations(request):
    page_title = 'Réalisations'
    nav_pages = make_nav(page_title)

    projects = Project.objects.all()
    pjlist = []
    for pj in projects:
        pjlist.append(pj)
    new_pj = pjlist[1]
    for i in range(10):
        pjlist.append(new_pj)
    pjlines = [pjlist[x:x+4] for x in range(0, len(pjlist), 4)]

    return render(request, 'website/realisations.html', locals())


def contact(request):
    page_title = 'Contact'
    nav_pages = make_nav(page_title)

    return render(request, 'website/contact.html', locals())


