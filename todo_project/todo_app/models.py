from datetime import datetime

from django.db import models

from todo_app.utils import date_shift


class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=48)
    surname = models.CharField(max_length=48)

    # @classmethod
    # def create(cls, name, surname):
    #     user = cls(name=name, surname=surname)
    #     return user


class Todo(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_completed = models.BooleanField(default=False, blank=False)
    title = models.CharField(max_length=200)
    content = models.TextField(max_length=1000)
    updated_at = models.DateTimeField(auto_now=True)
    complete_at = models.DateTimeField(default=date_shift)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
