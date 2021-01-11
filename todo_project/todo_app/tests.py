#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.test import TestCase

from .models import Todo, User


class TodoTestCase(TestCase):
    def setUp(self):

        self.user = User.objects.create(
            id=1, is_active=True, email="super_user@example.com", password="secret"
        )
        self.todo = Todo.objects.create(id=1, user=self.user)
        self.access_token = self.user.generate_access_token()

    def test_register(self):
        request = self.client.get("/register")

    def test_login(self):
        request = self.client.get("/login")

    def test_logout(self):
        request = self.client.get("/logout")

    def test_password_reset(self):
        request = self.client.get("/password_reset")

    def test_password_update(self):
        request = self.client.get("/password_update")
