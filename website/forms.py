#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
Docstring
"""
from __future__ import print_function, division
from __future__ import absolute_import, unicode_literals

from django import forms

from website.models import Message


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        exclude = ('isread', 'person',)