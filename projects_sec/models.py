from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.

class Projects_cover_info(models.Model):
    user = models.ManyToManyField(User)

    cover_name = models.CharField(max_length = 50)

    page_heading = models.CharField(max_length=100)
    page_subheading = models.TextField()

    

    def __str__(self):
        return self.cover_name

class Projects(models.Model):

    project_title = models.CharField(max_length=100)
    project_summary = models.TextField()
    
    github_link = models.CharField(max_length=500, blank=True,null=True)
    post_link = models.CharField(max_length=500, blank=True,null=True)
    

    def __str__(self):
        return self.project_title

    