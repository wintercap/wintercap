"""
Register all models in django admin
"""
from django.contrib import admin

from website.models import Category, Skill, Skillset, Person, Message
from website.models import UsedSkill, Project, Client

models_to_register = (
    Category,
    Skill,
    Skillset,
    Person,
    Message,
    UsedSkill,
    Project,
    Client,
)
for m in models_to_register:
    admin.site.register(m)