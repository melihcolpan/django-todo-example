from django.contrib.sessions.middleware import SessionMiddleware
from django.test import TestCase, RequestFactory, Client
from todo_app.models import User, Todo
from todo_app.views import Todos


class TodoTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        user = User.objects.create(id=1, name="Test", surname="Test")
        Todo.objects.create(id=1, title="Test Todo Title", content="Test todo content.", user=user)

    def test_get_todos(self):
        request = self.factory.get('/todo_app/todos')

        middleware = SessionMiddleware()
        middleware.process_request(request)
        request.session.save()

        response = Todos.as_view()(request)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Todo Title")

    def test_create_todos(self):
        request = self.factory.post('/todo_app/todos', content_type="application/json",
                                    data={"title": "New Todo Title", "content": "New todo content."})

        middleware = SessionMiddleware()
        middleware.process_request(request)
        request.session["user_id"] = 1
        request.session.save()

        response = Todos.as_view()(request)
        self.assertEqual(response.status_code, 200)

    def test_delete_todos(self):
        request = self.factory.delete('/todo_app/todos', content_type="application/json", data={"todo_id": 1})

        middleware = SessionMiddleware()
        middleware.process_request(request)
        request.session["user_id"] = 1
        request.session.save()

        response = Todos.as_view()(request)
        self.assertEqual(response.status_code, 200)

    def test_put_todos(self):
        request = self.factory.put('/todo_app/todos/1', content_type="application/json",
                                   data={"title": "Updated Test Title", "content": "Updated test content.",
                                         "todo_id": 1})

        middleware = SessionMiddleware()
        middleware.process_request(request)
        request.session["user_id"] = 1
        request.session.save()

        response = Todos.as_view()(request)
        self.assertEqual(response.status_code, 200)
