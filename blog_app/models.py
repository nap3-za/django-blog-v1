from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone


# Create your models here.

status_choices = [
    ('published', 'Published'),
    ('draft', 'Draft')
    ]


class Post(models.Model):
    
    title = models.CharField(max_length=200)
    page_title = models.CharField(max_length=250, null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=User)
    content = models.TextField()
    status = models.CharField(max_length=250, choices=status_choices, default='draft')
    date = models.DateField(default=timezone.now)
    
    
    def __str__(self):
        return str(self.title) + '   |   ' + str(self.author)
        
        
    def get_absolute_url(self):
        return reverse('homeview')
