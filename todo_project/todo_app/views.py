#!/usr/bin/python
# -*- coding: utf-8 -*-

import json

from django.db.utils import IntegrityError
from django.http import HttpResponse
from ratelimit.decorators import ratelimit

from todo_app import validations as v
from todo_app.middlewares import validator
from todo_app.models import User


@validator(v.validate_register)
@ratelimit(key="ip", rate="1/m")
def register(request):
    _in = json.loads(request.body.decode("utf-8"))

    try:
        User.objects.create(**_in)
    except IntegrityError:
        return HttpResponse(status=409)

    # TODO: Send verification email.

    return HttpResponse(status=201)


@validator(v.validate_verification)
def verification(request):
    pass


@validator(v.validate_login)
def login(request):
    pass


@validator(v.validate_logout)
def logout(request):
    pass


@validator(v.validate_password_reset)
def password_reset(request):
    pass


@validator(v.validate_password_update)
def password_update(request):
    pass
