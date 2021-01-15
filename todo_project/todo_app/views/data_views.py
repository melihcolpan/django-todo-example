#!/usr/bin/python
# -*- coding: utf-8 -*-

import json

import jwt
from django.db.utils import IntegrityError
from django.http import HttpResponse, JsonResponse
from ratelimit.decorators import ratelimit

from todo_app import validations as v
from todo_app.consts import HOST_ADDR, JWT_ALGORITHM, VERIFICATION_JWT_SECRET
from todo_app.middlewares import login_required, validator
from todo_app.models import Blacklist, Todo, User
from todo_app.utils import JSONSerializer
from todo_app.validations import validate_update_todo


@login_required
def get_todos(request):
    user_id = request.session["user"]["user_id"]

    todos = Todo.objects.filter(user=user_id).all()
    rs = JSONSerializer().serialize(todos)

    return JsonResponse({"data": rs})


@login_required
def get_todo(request, todo_id):
    user_id = request.session["user"]["user_id"]

    todo = Todo.objects.filter(id=todo_id, user=user_id).get()
    rs = JSONSerializer().serialize([todo])

    return JsonResponse({"data": json.loads(rs)[0]})


@login_required
@validator(validate_update_todo)
def update_todo(request, todo_id):
    _in = json.loads(request.body.decode("utf-8"))
    user_id = request.session["user"]["user_id"]

    Todo.objects.filter(id=todo_id, user=user_id).update(**_in)
    return HttpResponse(status=200)


@login_required
@validator(validate_update_todo)
def post_todo(request):
    _in = json.loads(request.body.decode("utf-8"))
    user_id = request.session["user"]["user_id"]

    Todo.objects.create(**_in, user_id=user_id)
    return HttpResponse(status=201)


@login_required
def delete_todo(request, todo_id):
    user_id = request.session["user"]["user_id"]

    Todo.objects.filter(id=todo_id, user=user_id).delete()
    return HttpResponse(status=204)
