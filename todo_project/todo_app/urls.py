#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.urls import path

from todo_app.views import auth_views, data_views


def todo_id_views(request, todo_id):
    if request.method == "PUT":
        return data_views.update_todo(request, todo_id)
    elif request.method == "DELETE":
        return data_views.delete_todo(request, todo_id)
    elif request.method == "GET":
        return data_views.get_todo(request, todo_id)
    else:
        return HttpResponse(status=405)


def todo_views(request):
    if request.method == "POST":
        return data_views.post_todo(request)
    elif request.method == "GET":
        return data_views.get_todos(request)
    else:
        return HttpResponse(status=405)


urlpatterns = [
    path("auth/register", auth_views.register, name="register"),
    path("auth/login", auth_views.login, name="login"),
    path("auth/logout", auth_views.logout, name="logout"),
    path("auth/verification", auth_views.verification, name="verification"),
    path("auth/password/reset", auth_views.password_reset, name="password_reset"),
    path(
        "auth/password/reset/verification",
        auth_views.password_reset_verification,
        name="password_verify",
    ),
    path("auth/password/update", auth_views.password_update, name="password_update"),
    path("data/todos", todo_views, name="get_todos"),
    path("data/todos", todo_views, name="post_todo"),
    path("data/todos/<int:todo_id>", todo_id_views, name="get_todo"),
    path("data/todos/<int:todo_id>", todo_id_views, name="update_todo"),
    path("data/todos/<int:todo_id>", todo_id_views, name="delete_todo"),
]
