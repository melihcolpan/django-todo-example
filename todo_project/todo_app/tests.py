#!/usr/bin/python
# -*- coding: utf-8 -*-

from datetime import datetime, timedelta

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
            "/auth/logout", data=data, content_type="application/json", **self.headers
        )
        self.assertEqual(200, request.status_code)

    def test_password_reset(self):
        data = {"email": self.user.email}
        request = self.client.post(
            "/auth/password/reset", data=data, content_type="application/json"
        )
        self.assertEqual(200, request.status_code)

    def test_password_reset_verification(self):
        data = {"new_password": "new-secret"}
        request = self.client.post(
            "/auth/password/reset/verification",
            data=data,
            content_type="application/json",
            **self.headers,
        )
        self.assertEqual(200, request.status_code)

    def test_password_update(self):
        data = {"new_password": "new-secret", "old_password": self.user.password}
        request = self.client.post(
            "/auth/password/update",
            data=data,
            content_type="application/json",
            **self.headers,
        )
        self.assertEqual(200, request.status_code)
        user = User.objects.filter(id=self.user.id).get()
        print(user.password)
        self.assertEqual(data["new_password"], user.password)

    def test_get_todos(self):
        request = self.client.get("/data/todos", **self.headers)
        self.assertEqual(200, request.status_code)
        rs = request.json()
        self.assertIn("data", rs)

    def get_todo(self):
        request = self.client.get(f"/data/todos/{self.todo.id}", **self.headers)
        self.assertEqual(200, request.status_code)
        rs = request.json()
        self.assertIn("data", rs)

    def update_todo(self):
        data = {
            "is_completed": True,
            "is_removed": False,
            "title": "Updated Title",
            "content": "Updated Content",
            "expire_at": (datetime.now() + timedelta(days=30)).__format__(
                "%Y-%m-%d %H:%M:%S"
            ),
        }
        request = self.client.put(
            f"/data/todos/{self.todo.id}",
            data=data,
            content_type="application/json",
            **self.headers,
        )
        self.assertEqual(200, request.status_code)
        todo = Todo.objects.filter(id=self.todo.id).get()
        self.assertEqual(data["is_completed"], todo.is_completed)
        self.assertEqual(data["is_removed"], todo.is_removed)
        self.assertEqual(data["title"], todo.title)
        self.assertEqual(data["content"], todo.content)
        self.assertEqual(
            data["expire_at"], todo.expire_at.__format__("%Y-%m-%d %H:%M:%S")
        )

    def post_todo(self):
        data = {
            "is_completed": True,
            "is_removed": False,
            "title": "Updated Title",
            "content": "Updated Content",
            "expire_at": (datetime.now() + timedelta(days=30)).__format__(
                "%Y-%m-%d %H:%M:%S"
            ),
        }
        request = self.client.post(
            f"/data/todos", data=data, content_type="application/json", **self.headers
        )
        self.assertEqual(201, request.status_code)

    def delete_todo(self):
        request = self.client.delete(
            f"/data/todos/{self.todo.id}",
            content_type="application/json",
            **self.headers,
        )
        self.assertEqual(204, request.status_code)
