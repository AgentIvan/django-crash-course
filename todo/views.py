from django.http.response import HttpResponse
from django.shortcuts import render

from .models import Todo


def todo_list(request):
    todos = Todo.objects.all()
    context = {"todo_list": todos}
    return render(request, "todo/todo_list.html", context)
