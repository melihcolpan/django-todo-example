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
        data = {"username": "Test Username", "email": "a@b.com", "password": "secret"}
        request = self.client.post(
            "/auth/register", data=data, content_type="application/json"
        )

        self.assertEqual(201, request.status_code)

    def test_verification(self):
        request = self.client.get("/auth/login")

    def test_login(self):
        data = {"email": self.user.email, "password": self.user.password}
        request = self.client.post(
            "/auth/login", data=data, content_type="application/json"
        )
        self.assertEqual(200, request.status_code)

        result = request.json()
        self.assertIn("data", result)
        self.assertIn("access_token", result["data"])

    def test_logout(self):
        data = {"refresh_token": self.user.generate_refresh_token()}
        request = self.client.post(
            "/auth/logout", data=data, content_type="application/json"
        )
        self.assertEqual(200, request.status_code)

    def test_password_reset(self):
        request = self.client.get("/auth/password_reset")

    def test_password_update(self):
        request = self.client.get("/auth/password_update")
