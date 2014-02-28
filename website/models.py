#-*- coding: utf-8 -*-
from __future__ import print_function, division
from __future__ import absolute_import, unicode_literals
from django.db.models.signals import post_delete
from django.dispatch import receiver

import os

from django.db import models


def get_image_path(instance, filename):
    server_filename = str(instance.id) + '_' + filename
    return os.path.join('screenshots', server_filename)


class Client(models.Model):
    name = models.CharField(verbose_name='Nom du client', max_length=50)
    url = models.URLField(verbose_name='URL du client')

    def __unicode__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(verbose_name='Nom du projet', max_length=50)
    desc = models.TextField(verbose_name='Description', max_length=5000)
    image = models.ImageField(verbose_name="Capture d'écran",
                              upload_to=get_image_path)
    url = models.URLField(verbose_name='URL du projet')
    client = models.ForeignKey('Client')

    def __unicode__(self):
        return self.name


@receiver(post_delete, sender=Project)
def project_post_delete_handler(sender, **kwargs):
    project = kwargs['instance']
    storage, path = project.image.storage, project.image.path
    storage.delete(path)


class Techno(models.Model):
    name = models.CharField(verbose_name='Nom de la techno', max_length=50)
    desc = models.TextField(verbose_name='Description', max_length=500)
    url = models.URLField(verbose_name='URL de la techno')

    def __unicode__(self):
        return self.name


class Message(models.Model):
    name = models.CharField(verbose_name='Nom du contact', max_length=50)
    email = models.EmailField(verbose_name='Email du contact')
    message = models.TextField(verbose_name='Message', max_length=500)
    read = models.BooleanField(verbose_name='Lu', default=False)

    def __unicode__(self):
        return self.name


class CompetenceCategory(models.Model):
    name = models.CharField(verbose_name='Nom de la catégorie', max_length=50)

    def __unicode__(self):
        return self.name


class Competence(models.Model):
    name = models.CharField(verbose_name='Nom de la compétence', max_length=50)
    desc = models.TextField(verbose_name='Descriptif', max_length=500)
    level = models.SmallIntegerField(verbose_name='Niveau de maîtrise')
    category = models.ForeignKey('CompetenceCategory')

    def __unicode__(self):
        return self.name