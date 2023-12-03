from django.urls import path

from . import views

app_name = "todos"

urlpatterns = [
    path("", views.index, name="index"),

    path("new_todo/", views.new_todo, name="new_todo"),
    path("new_todo_list/", views.new_todo_list, name="new_todo_list"),
    path("<id>/", views.detail, name="detail"),

]