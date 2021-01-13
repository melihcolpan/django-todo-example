#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.urls import path

from todo_app import views

urlpatterns = [
    path("auth/register", views.register, name="register"),
    path("auth/login", views.login, name="login"),
    path("auth/logout", views.logout, name="logout"),
    path("auth/verification", views.verification, name="verification"),
    path("auth/password_reset", views.password_reset, name="password_reset"),
    path("auth/password_update", views.password_update, name="password_update"),
]
