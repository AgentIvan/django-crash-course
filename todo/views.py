from django.http.response import HttpResponse
from django.shortcuts import render


def todo_list(request):
    return render(request, "todo_list2.html")
