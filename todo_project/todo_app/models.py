#!/usr/bin/python
# -*- coding: utf-8 -*-

from datetime import datetime, timedelta

import jwt
from django.db import models

from todo_app.consts import (
    JWT_ALGORITHM,
    JWT_EXP_DELTA_SECONDS,
    JWT_SECRET,
    REFRESH_JWT_EXP_DELTA_SECONDS,
    REFRESH_JWT_SECRET,
    VERIFICATION_JWT_EXP_DELTA_SECONDS,
    VERIFICATION_JWT_SECRET,
)


class User(models.Model):
    id = models.AutoField(primary_key=True)
    is_active = models.BooleanField(default=True)
    is_verified = models.BooleanField(default=False)
    username = models.CharField(max_length=48)
    email = models.CharField(max_length=48, unique=True)
    password = models.CharField(max_length=48)
    name = models.CharField(max_length=48)
    surname = models.CharField(max_length=48)

    def generate_token(self, token_type="access"):
        if token_type == "access":
            exp_delta_seconds = JWT_EXP_DELTA_SECONDS
            secret = JWT_SECRET
        elif token_type == "refresh":
            exp_delta_seconds = REFRESH_JWT_EXP_DELTA_SECONDS
            secret = REFRESH_JWT_SECRET
        else:
            exp_delta_seconds = VERIFICATION_JWT_EXP_DELTA_SECONDS
            secret = VERIFICATION_JWT_SECRET

        payload = {
            "user_id": self.id,
            "email": self.email,
            "is_active": self.is_active,
            "exp": datetime.utcnow() + timedelta(seconds=exp_delta_seconds),
        }
        return jwt.encode(payload, secret, JWT_ALGORITHM)


class Todo(models.Model):
    id = models.AutoField(primary_key=True)
    is_completed = models.BooleanField(default=False, blank=False)
    is_removed = models.BooleanField(default=False, blank=False)
    title = models.CharField(max_length=200)
    content = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    expire_at = models.DateTimeField(null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Blacklist(models.Model):
    id = models.AutoField(primary_key=True)
    refresh_token = models.CharField(max_length=255)
