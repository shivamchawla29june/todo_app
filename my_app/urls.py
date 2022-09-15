from django.urls import path
from django.conf import settings
from . import views

urlpatterns = [
    path('', views.TodoApp,name="Todo"),
    path('add_todo/', views.add_todo,name="add_todo"),
    path('delete_todo/<int:todo_id>/', views.delete_todo,name="delete_todo"),
]
