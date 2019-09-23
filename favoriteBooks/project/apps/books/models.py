from django.db import models
from apps.application.models import *
from datetime import datetime
# Create your models here.

class BookManager(models.Manager):
    def bookValidator(self, postData):
        errors = {}
        if len(postData['title']) < 1:
            errors['title'] = "Title is required"
        if len(postData['description']) < 5:
            errors['desc'] = "Description must be at least 5 characters"
        return errors

class Book(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    usersWhoLike = models.ManyToManyField(User, related_name="likedBooks")
    uploader = models.ForeignKey(User, related_name="booksUploaded")
    objects = BookManager()
