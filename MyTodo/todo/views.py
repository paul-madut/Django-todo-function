from django.shortcuts import render, redirect
from django.http import Http404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from .models import Todo
from . import forms

loginUrl = '/accounts/login/' 


login_required(login_url=loginUrl)
def index(request):
    todo_list = Todo.objects.order_by("title")[:5]

    context = {
        "todo_list" : todo_list,
    }

    return render(request,"todo/index.html",context)

@login_required(login_url=loginUrl)
def detail(request,id):
    try:
        todo = Todo.objects.get(pk=id)
    except Todo.DoesNotExist:
        raise Http404("Todo does not exist")
    return render(request, "todo/detail.html", {"todo":todo})

@login_required(login_url=loginUrl)
def new_todo(request):
    if request.method == "POST":
        form = forms.TodoForm(request.POST)
        if form.is_valid():
            todo_insance = form.save(commit=False)
            todo_insance.author = request.user
            todo_insance.save()
           
            return redirect("todos:index")
    else:
        form = forms.TodoForm()
    return render(request, "todo/new_todo.html", {"form":form})
    

@login_required(login_url=loginUrl)
def new_todo_list(request):
    if request.method == "POST":
        form = forms.TodoListForm(request.POST)
        if form.is_valid():
           todo_list_instance = form.save(commit=False)
           todo_list_instance.author = request.user
           todo_list_instance.save()
           return redirect("todos:index")
    else:
        form = forms.TodoListForm()
    return render(request, "todo/new_todo_list.html", {"form":form})
    
