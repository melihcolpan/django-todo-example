#!/usr/bin/python
# -*- coding: utf-8 -*-

from datetime import datetime

from cerberus import Validator


def validate_register(_in):
    schema = {
        "username": {
            "type": "string",
            "maxlength": 24,
            "nullable": False,
            "required": True,
        },
        "email": {
            "type": "string",
            "maxlength": 48,
            "nullable": False,
            "required": True,
            "regex": "^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$",
        },
        "password": {
            "type": "string",
            "maxlength": 16,
            "nullable": False,
            "required": True,
        },
    }
    v = Validator(schema)
    is_valid = v.validate(_in)
    return is_valid, v.errors


def validate_verification(_in):
    schema = {
        "verification": {
            "type": "list",
            "maxlength": 1,
            "minlength": 1,
            "nullable": False,
            "required": True,
            "items": [{"type": "string"}],
        },
    }

    v = Validator(schema)
    is_valid = v.validate(_in)
    return is_valid, v.errors


def validate_login(_in):
    schema = {
        "email": {
            "type": "string",
            "maxlength": 48,
            "nullable": False,
            "required": True,
            "regex": "^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$",
        },
        "password": {
            "type": "string",
            "maxlength": 16,
            "nullable": False,
            "required": True,
        },
    }

    v = Validator(schema)
    is_valid = v.validate(_in)
    return is_valid, v.errors


def validate_logout(_in):
    schema = {
        "refresh_token": {
            "type": "string",
            "maxlength": 255,
            "nullable": False,
            "required": True,
        },
    }

    v = Validator(schema)
    is_valid = v.validate(_in)
    return is_valid, v.errors


def validate_password_reset(_in):
    schema = {
        "email": {
            "type": "string",
            "maxlength": 48,
            "nullable": False,
            "required": True,
            "regex": "^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$",
        },
    }

    v = Validator(schema)
    is_valid = v.validate(_in)
    return is_valid, v.errors


def validate_password_reset_verification(_in):
    schema = {
        "new_password": {
            "type": "string",
            "maxlength": 48,
            "nullable": False,
            "required": True,
        },
    }

    v = Validator(schema)
    is_valid = v.validate(_in)
    return is_valid, v.errors


def validate_password_update(_in):
    schema = {
        "old_password": {
            "type": "string",
            "maxlength": 48,
            "nullable": False,
            "required": True,
        },
        "new_password": {
            "type": "string",
            "maxlength": 48,
            "nullable": False,
            "required": True,
        },
    }

    v = Validator(schema)
    is_valid = v.validate(_in)
    return is_valid, v.errors


def validate_update_todo(_in):
    schema = {
        "is_completed": {
            "type": "boolean",
            "maxlength": 48,
            "nullable": False,
            "required": False,
        },
        "is_removed": {
            "type": "boolean",
            "maxlength": 48,
            "nullable": False,
            "required": False,
        },
        "title": {
            "type": "string",
            "maxlength": 48,
            "nullable": False,
            "required": False,
        },
        "content": {
            "type": "string",
            "maxlength": 48,
            "nullable": False,
            "required": False,
        },
        "expire_at": {
            "type": "datetime",
            "coerce": lambda s: datetime.strptime(s, "%Y-%m-%d %H:%M:%S"),
            "nullable": False,
            "required": False,
        },
    }

    v = Validator(schema)
    is_valid = v.validate(_in)
    return is_valid, v.errors
