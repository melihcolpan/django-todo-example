#!/usr/bin/python
# -*- coding: utf-8 -*-

from cerberus import Validator


def validate_register(_in):
    schema = {}

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
