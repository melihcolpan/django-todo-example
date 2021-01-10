#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.db import models


class User(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=48)
    name = models.CharField(max_length=48)
    surname = models.CharField(max_length=48)
    email = models.CharField(max_length=48)
    password = models.CharField(max_length=48)


class Todo(models.Model):
    id = models.AutoField(primary_key=True)
    is_completed = models.BooleanField(default=False, blank=False)
    title = models.CharField(max_length=200)
    content = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    expire_at = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
