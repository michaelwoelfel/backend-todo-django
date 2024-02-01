from django.db import models
from django.contrib.auth.models import User
from datetime import datetime  



class Todo(models.Model):
  
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    date = models.DateField( default=datetime.now())
    title = models.CharField(max_length=100)
    description = models.TextField()
    my_field = models.BooleanField(default=False)
    
    def __str__(self):
        return f'{self.id} {self.title}'