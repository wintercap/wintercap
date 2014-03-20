#-*- coding: utf-8 -*-
from __future__ import print_function, division
from __future__ import absolute_import, unicode_literals
from django.db.models.signals import post_delete
from django.dispatch import receiver

import os

from django.db import models


def get_image_path(instance, filename):
    if isinstance(instance, Client):
        folder = 'clients'
    elif isinstance(instance, Project):
        folder = 'projects'
    elif isinstance(instance, Person):
        folder = 'people'
    else:
        folder = 'misc'
    server_filename = unicode(instance).replace(' ', '_') + '_' + filename
    return os.path.join('img', folder, server_filename)


class Client(models.Model):
    name = models.CharField(verbose_name='Nom du client', max_length=50)
    description = models.TextField(verbose_name='Description', max_length=500,
                                   blank=True)
    url = models.URLField(verbose_name='URL du client', blank=True)
    image = models.ImageField(verbose_name='Logo', upload_to=get_image_path,
                              blank=True)

    def __unicode__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(verbose_name='Nom du projet', max_length=50)
    description = models.TextField(verbose_name='Description', max_length=5000)
    url = models.URLField(verbose_name='URL du projet')
    image = models.ImageField(verbose_name="Capture d'écran",
                              upload_to=get_image_path, blank=True)
    client = models.ForeignKey('Client')

    def __unicode__(self):
        return self.name


@receiver(post_delete, sender=Project)
def project_post_delete_handler(sender, **kwargs):
    project = kwargs['instance']
    storage, path = project.image.storage, project.image.path
    storage.delete(path)


class Skill(models.Model):
    name = models.CharField(verbose_name='Nom de la compétence', max_length=50)
    description = models.TextField(verbose_name='Description', max_length=500,
                                   blank=True)
    category = models.ForeignKey('Category')

    def __unicode__(self):
        return self.name


class Person(models.Model):
    firstname = models.CharField(verbose_name='Prénom', max_length=50)
    lastname = models.CharField(verbose_name='Nom', max_length=50)
    nickname = models.CharField(verbose_name='Pseudonyme', max_length=50,
                                blank=True)
    email = models.EmailField(verbose_name='Email')
    url = models.URLField(verbose_name='Site perso', blank=True)
    image = models.ImageField(verbose_name='Photo', upload_to=get_image_path,
                              blank=True)

    def __unicode__(self):
        if self.nickname:
            return self.nickname
        else:
            return self.firstname + ' ' + self.lastname


class Message(models.Model):
    sender = models.EmailField(verbose_name='Email du contact')
    subject = models.CharField(verbose_name='Sujet', max_length=50)
    message = models.TextField(verbose_name='Message', max_length=500)
    isread = models.BooleanField(verbose_name='Lu', default=False)
    person = models.ForeignKey('Person')

    def __unicode__(self):
        return 'from ' + unicode(self.sender) + ': ' + unicode(self.subject)


class Category(models.Model):
    name = models.CharField(verbose_name='Nom de la catégorie', max_length=50)
    description = models.TextField(verbose_name='Description', max_length=500,
                                   blank=True)

    def __unicode__(self):
        return self.name


class Skillset(models.Model):
    level = models.SmallIntegerField(verbose_name='Niveau de maîtrise')
    skill = models.ForeignKey('Skill')
    person = models.ForeignKey('Person')

    def __unicode__(self):
        return unicode(self.person) + ': ' + self.skill.name


class UsedSkill(models.Model):
    skillset = models.ForeignKey('Skillset')
    project = models.ForeignKey('Project')

    def __unicode__(self):
        return self.project.name + ': ' + unicode(self.skillset)