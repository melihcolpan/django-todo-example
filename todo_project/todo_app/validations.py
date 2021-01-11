#!/usr/bin/python
# -*- coding: utf-8 -*-

from cerberus import Validator


def validate_register(_in):
    schema = {
        "username": {
            "type": "string",
            "maxlength": 24,
            "nullable": False,
            "requreid": True,
        },
        "email": {
            "type": "string",
            "maxlength": 48,
            "nullable": False,
            "requreid": True,
            "regex": "^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$",
        },
        "password": {
            "type": "string",
            "maxlength": 48,
            "nullable": False,
            "requreid": True,
        },
    }
    v = Validator(schema)
    is_valid = v.validate(_in)
    return is_valid, v.errors


def validate_login(_in):
    schema = {}

    v = Validator(schema)
    is_valid = v.validate(_in)
    return is_valid, v.errors


def validate_logout(_in):
    schema = {}

    v = Validator(schema)
    is_valid = v.validate(_in)
    return is_valid, v.errors


def validate_password_reset(_in):
    schema = {}

    v = Validator(schema)
    is_valid = v.validate(_in)
    return is_valid, v.errors


def validate_password_update(_in):
    schema = {}

    v = Validator(schema)
    is_valid = v.validate(_in)
    return is_valid, v.errors
