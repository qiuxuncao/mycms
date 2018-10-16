# coding:utf-8
from django.db import models
from tinymce.models import HTMLField

# Create your models here.


class BlogPost(models.Model):

    title = models.CharField(max_length=150)
    body = HTMLField()
    timestamp = models.DateTimeField()
    tags = models.CharField(max_length=100)
    views_count = models.TextField()
    comments_count = models.TextField()
    auth = models.TextField(default='谷晨')
    address = models.CharField(max_length=100, default='西安')