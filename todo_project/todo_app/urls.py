#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.urls import path

from .views import Todos

urlpatterns = [
    path("todos/", Todos.as_view(), name="todos_one"),
    path("todos/<int:key_id>/", Todos.as_view(), name="todos_two"),
    path("todos/<int:pk>", Todos.as_view(), name="todos_three"),
]
