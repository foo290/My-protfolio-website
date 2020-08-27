from django.db import models
from django.contrib.auth.models import User
from PIL import Image


# Create your models here.

class PrimaryUser(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE)

    name = models.CharField(max_length=50)
    fancy_name = models.CharField(max_length=50)
    bio = models.TextField()
    status = models.TextField()


    location = models.CharField(max_length=20)   
    twitter = models.URLField(max_length=300)
    github = models.URLField(max_length=300)
    discord = models.URLField(max_length=300)
    linkdin = models.URLField(max_length=300)
    email_id = models.EmailField(max_length = 50)

    recent_project_title = models.CharField(max_length=100)
    recent_project_sub_title = models.CharField(max_length=150)
    recent_project_summary = models.TextField()

    def __str__(self):
        return str(self.username)
