#!/usr/bin/python
# -*- coding: utf-8 -*-

import jwt
import json
from json import JSONDecodeError

from django.http import HttpResponse


from todo_app.consts import JWT_SECRET, JWT_ALGORITHM


def login_required(func):
    def wrapper(*args, **kwargs):
        request = args[0]

        try:
            jwt_token = request.META["Authorization"].replace("Bearer ", "")
            data = jwt.decode(jwt_token, JWT_SECRET, algorithms=[JWT_ALGORITHM])

            if not data["is_active"]:
                return HttpResponse("Your account suspended.", status=401)

            del data["exp"]
            request.session["user"] = data

        except Exception as e:
            return HttpResponse(f"Middleware unauthorized. {e.args[0]}", status=401)

        return func(*args, **kwargs)

    return wrapper


def validator(schema=None):
    def decorator(func):
        def wrapper(*args, **kwargs):
            request = args[0]

            if request.method == "GET":
                _in = dict(request.GET)
                valid, errors = schema(_in)
                if not valid:
                    return HttpResponse(errors, status=422)

            elif (
                request.method == "POST"
                or request.method == "PUT"
                or request.method == "DELETE"
            ):
                try:
                    _in = json.loads(request.body.decode("utf-8"))
                except JSONDecodeError:
                    return HttpResponse("Input JSON not serializable.", status=422)
                else:
                    valid, errors = schema(_in)
                    if not valid:
                        return HttpResponse(errors, status=422)

            return func(*args, **kwargs)

        return wrapper

    return decorator
