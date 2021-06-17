from django.db import models
from datetime import datetime

# Create your models here.


class User(models.Model):
    user_name = models.CharField(max_length=25)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email = models.EmailField(max_length=25)
    password = models.CharField(max_length=25)

    class Meta:
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.user_name


class Post(models.Model):
    post_content = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Posts'

    def __str__(self):
        return str(self.created_at)
