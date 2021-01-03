#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect
from django.template import loader
from django.views.generic import TemplateView
from todo_app.models import Todo, User
import json


class Todos(TemplateView):

    def get(self, request, *args, **kwargs):

        # Get user session.
        user_id = request.session.get('user_id', None)

        # Set if no session.
        if not user_id:
            user = User.objects.create(name="Test", surname="Test")
            request.session['user_id'] = user.id

        # Get all to-do objects.
        data = Todo.objects.all()

        # Render index template.
        template = loader.get_template('todo/index.html')

        # Make content ready.
        context = {'todo_list': data}

        # Render and return template.
        return HttpResponse(template.render(context, request))

    @csrf_exempt
    def post(self, request, *args, **kwargs):

        # Get user id.
        user_id = request.session.get('user_id', None)

        # If no user before, redirect to main page.
        if not user_id:
            return redirect("/todo_app/todos")

        # Get request body.
        _in = json.loads(request.body.decode('utf-8'), )

        # Check parameters.
        if not _in.get("title") and not _in.get("content"):

            # Return error if any missing parameter.
            return JsonResponse({"error": f"Invalid Error"}, status=422)

        # Create to-do for user.
        Todo.objects.create(title=_in['title'], content=_in['content'], user_id=user_id)

        # Return success.
        return JsonResponse({"message": "OK"})

    def delete(self, request, *args, **kwargs):

        # Get user id.
        user_id = request.session.get('user_id', None)

        # If no user before, redirect to main page.
        if not user_id:
            return redirect("/todo_app/todos")

        # Get request body.
        _in = json.loads(request.body.decode('utf-8'), )

        # Check parameters.
        if not _in.get("todo_id"):

            # Return error if any missing parameter.
            return JsonResponse({"error": f"Invalid Error"}, status=422)

        # Create to-do for user. Only own to-do items.
        Todo.objects.filter(id=_in["todo_id"], user_id=user_id).delete()

        # Return success.
        return JsonResponse({"message": "OK"})

    def put(self, request, *args, **kwargs):

        # Get user id.
        user_id = request.session.get('user_id', None)

        # If no user before, redirect to main page.
        if not user_id:
            return redirect("/todo_app/todos")

        # Get request body.
        _in = json.loads(request.body.decode('utf-8'), )

        # Able to change parameters.
        parameters = ["is_completed", "title", "content", "complete_at", "todo_id"]

        # Check parameters.
        if set(_in.keys()) - set(parameters) or "todo_id" not in _in.keys():

            # Return error if any missing parameter.
            return JsonResponse({"error": f"Invalid Error"}, status=422)

        todo_id = _in.pop("todo_id")

        # Create to-do for user. Only own to-do items.
        Todo.objects.filter(id=todo_id, user_id=user_id).update(**_in)

        # Return success.
        return JsonResponse({"message": "OK"})
