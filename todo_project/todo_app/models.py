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
    REFRESH_JWT_SECRET, VERIFICATION_JWT_EXP_DELTA_SECONDS, HOST_ADDR, VERIFICATION_JWT_SECRET,
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

    def generate_access_token(self):
        payload = {
            "user_id": self.id,
            "email": self.email,
            "is_active": self.is_active,
            "exp": datetime.utcnow() + timedelta(seconds=JWT_EXP_DELTA_SECONDS),
        }
        return jwt.encode(payload, JWT_SECRET, JWT_ALGORITHM)

    def generate_refresh_token(self):
        payload = {
            "user_id": self.id,
            "email": self.email,
            "is_active": self.is_active,
            "exp": datetime.utcnow() + timedelta(seconds=REFRESH_JWT_EXP_DELTA_SECONDS),
        }
        return jwt.encode(payload, REFRESH_JWT_SECRET, JWT_ALGORITHM)

    def generate_verification_url(self):
        payload = {
            "user_id": self.id,
            "email": self.email,
            "is_active": self.is_active,
            "exp": datetime.utcnow() + timedelta(seconds=VERIFICATION_JWT_EXP_DELTA_SECONDS),
        }
        verification = jwt.encode(payload, VERIFICATION_JWT_SECRET, JWT_ALGORITHM)
        return f"{HOST_ADDR}/?verification={verification}"


class Todo(models.Model):
    id = models.AutoField(primary_key=True)
    is_completed = models.BooleanField(default=False, blank=False)
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
