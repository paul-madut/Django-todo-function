from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class TodoList(models.Model):
     title = models.CharField(max_length=100, unique=True)
     author = models.ForeignKey(User, default=None, on_delete=models.CASCADE , blank=True, null=True)

     def __str__(self):
        return self.title
     
     class Meta:
        ordering = ["title"]
     

     
class Todo(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    isDone = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=timezone.now)
    todo_list = models.ForeignKey( TodoList, default=None,on_delete=models.CASCADE , blank=True, null=True)
    author = models.ForeignKey(User, default=None, on_delete=models.CASCADE , blank=True, null=True)



    def __str__(self) -> str:
        return self.title
    
    class Meta:
        ordering = ["-created_date"]
