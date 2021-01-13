#!/usr/bin/python
# -*- coding: utf-8 -*-

import json

import jwt
from django.db.utils import IntegrityError
from django.http import HttpResponse, JsonResponse
from ratelimit.decorators import ratelimit

from todo_app import validations as v
from todo_app.consts import JWT_ALGORITHM, VERIFICATION_JWT_SECRET
from todo_app.middlewares import login_required, validator
from todo_app.models import Blacklist, User


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
    verification_token = request.GET.get("verification")
    data = jwt.decode(
        verification_token, VERIFICATION_JWT_SECRET, algorithms=[JWT_ALGORITHM]
    )

    User.objects.filter(id=data["user_id"]).update(**{"is_verified": True})
    return HttpResponse(status=200)


@validator(v.validate_login)
def login(request):
    _in = json.loads(request.body.decode("utf-8"))

    try:
        user = User.objects.filter(email=_in["email"], password=_in["password"]).get()
        rs = {
            "data": {
                "access_token": user.generate_token(),
                "refresh_token": user.generate_token(token_type="refresh"),
            }
        }
        return JsonResponse(rs)

    except User.DoesNotExist:
        return HttpResponse(status=404)


@validator(v.validate_logout)
def logout(request):
    _in = json.loads(request.body.decode("utf-8"))

    check = Blacklist.objects.filter(refresh_token=_in["refresh_token"]).exists()
    if check:
        return HttpResponse(status=409)

    Blacklist.objects.create(**_in)
    return HttpResponse(status=200)


@validator(v.validate_password_reset)
def password_reset(request):
    return NotImplemented


@login_required
@validator(v.validate_password_update)
def password_update(request):
    # TODO: Check old password and keep hash passwords.
    _in = json.loads(request.body.decode("utf-8"))

    User.objects.filter(id=request.session.get("user").get("id")).update(
        **{"password": _in["new_password"]}
    )
    return HttpResponse(status=200)
