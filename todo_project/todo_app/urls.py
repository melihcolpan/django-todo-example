#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.urls import path

from todo_app import views

urlpatterns = [
    path("auth/register", views.register, name="register"),
    path("auth/login", views.login, name="login"),
    path("auth/logout", views.logout, name="logout"),
    path("auth/verification", views.verification, name="verification"),
    path("auth/password/reset", views.password_reset, name="password_reset"),
    path(
        "auth/password/reset/verification",
        views.password_reset_verification,
        name="password_verify",
    ),
    path("auth/password/update", views.password_update, name="password_update"),
]
