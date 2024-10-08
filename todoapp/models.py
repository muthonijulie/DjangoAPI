from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Todo(models.Model):
     title=models.CharField(max_length=100)
     content=models.CharField(max_length=255)
     created_at=models.DateField()
     task_by=models.ForeignKey(User,related_name='todo',on_delete=models.CASCADE)

     def __str__(self):
          return self.title