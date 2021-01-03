from django.urls import path, re_path

from . import views
from .views import Todos

urlpatterns = [
    path('todos/', Todos.as_view(), name='todos_one'),
    path('todos/<int:key_id>/', Todos.as_view(), name='todos_two'),

]
