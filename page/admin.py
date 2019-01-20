from django.contrib import admin
from .models import About, Project
from django.contrib.auth.models import User
from django.contrib.auth.models import Group

admin.site.register(About)
admin.site.register(Project)
admin.site.unregister(User)
admin.site.unregister(Group)
