from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse



class Post(models.Model):
    STATUS_CHOICES={
     ('draft','Draft'),   
     ('published','Published'), 
    }
    title = models.CharField(max_length=45)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    status =models.CharField(max_length=10,choices=STATUS_CHOICES,default='draft')


    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
      
    
   
      
