#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.urls import path

from .views import Todos

urlpatterns = [
    path("", Todos.as_view(), name="todos_one"),
]
