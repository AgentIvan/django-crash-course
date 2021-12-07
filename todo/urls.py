from django.urls import path

from .views import todo_detail, todo_list

app_name = "todos"

urlpatterns = [
    path("", todo_list),
    path("<id>/", todo_detail),
]
