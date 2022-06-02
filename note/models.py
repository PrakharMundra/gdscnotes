from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
   title=models.CharField(max_length=100)
   content=models.TextField()
   tag1=models.CharField(max_length=20)
   tag2=models.CharField(max_length=20)
   author=models.ForeignKey(User, on_delete=models.CASCADE)
   def __str__(self):
       return self.title

   def get_absolute_url(self):
       return reverse('note-home',kwargs={'username':self.author})    


