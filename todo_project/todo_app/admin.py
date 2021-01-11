#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.contrib import admin

from .models import User, Todo

admin.site.register(User)
admin.site.register(Todo)
