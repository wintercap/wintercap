#-*- coding: utf-8 -*-
"""
wintercap.fr website views
"""
from __future__ import print_function, division
from __future__ import absolute_import, unicode_literals
from collections import OrderedDict
from django.contrib import messages
from django.core.mail import send_mail

from django.shortcuts import render, redirect
from website.forms import MessageForm

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
    categories = Category.objects.all()
    for cat in categories:
        cat.skills = Skill.objects.filter(category=cat)
        for skill in cat.skills:
            skill.level = Skillset.objects.get(skill=skill, person__id=1).level
    return render(request, 'website/competences.html', locals())


def realisations(request):
    page_title = 'Réalisations'
    nav_pages = make_nav(page_title)
    projects = Project.objects.all()
    pjlist = []
    for pj in projects:
        pjlist.append(pj)
        pj.sklist = UsedSkill.objects.filter(project=pj)
    pjlines = [pjlist[x:x + 4] for x in range(0, len(pjlist), 4)]
    return render(request, 'website/realisations.html', locals())


def contact(request):
    page_title = 'Contact'
    nav_pages = make_nav(page_title)
    people = Person.objects.all()
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.isread = False
            message.person = Person.objects.get(id=1)
            message.save()
            message_with_sender = message.sender + '\n' + message.message
            # send_mail(message.subject, message_with_sender, message.sender,
            #           [message.person.email], fail_silently=False)
            messages.success(request, 'Votre message a bien été envoyé.')
            return redirect('website.views.contact')
    else:
        form = MessageForm()
    return render(request, 'website/contact.html', locals())


