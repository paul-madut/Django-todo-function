from django import forms
from . import models

class TodoForm(forms.ModelForm):

    title = forms.CharField(label="todo title", max_length=100)
    description = forms.CharField(label="description")
    todoList = forms.ModelChoiceField(queryset=models.TodoList.objects.all())

    class Meta:
        model = models.Todo
        fields = ['title', 'description']

class TodoListForm(forms.ModelForm):
    title = forms.CharField(label="todo list title", max_length=100)

    class Meta:
        model = models.TodoList
        fields = ['title']