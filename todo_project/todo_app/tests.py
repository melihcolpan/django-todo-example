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
        self.access_token = self.user.generate_token()
        self.headers = {"Authorization": f"Bearer {self.user.generate_token()}"}

    def test_register(self):
        data = {"username": "Test Username", "email": "a@b.com", "password": "secret"}
        request = self.client.post(
            "/auth/register", data=data, content_type="application/json"
        )

        self.assertEqual(201, request.status_code)

    def test_verification(self):
        request = self.client.get(
            f"/auth/verification?verification={self.user.generate_token(token_type='verification')}"
        )

        self.assertEqual(200, request.status_code)
        user = User.objects.filter(id=self.user.id).get()
        self.assertTrue(user.is_verified)

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
        data = {"refresh_token": self.user.generate_token(token_type="refresh")}
        request = self.client.post(
            "/auth/logout", data=data, content_type="application/json"
        )
        self.assertEqual(200, request.status_code)

    def test_password_reset(self):
        request = self.client.get("/auth/password_reset")

    def test_password_update(self):
        data = {"new_password": "new-secret", "old_password": self.user.password}
        request = self.client.post(
            "/auth/password_update",
            data=data,
            content_type="application/json",
            **self.headers,
        )
        print(request.status_code)
        print(request.content)
