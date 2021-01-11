#!/usr/bin/python
# -*- coding: utf-8 -*-

from todo_app import validations as v
from todo_app.middlewares import validator


@validator(v.validate_register)
def register(request):
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
