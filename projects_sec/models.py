from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.

class Projects_cover_info(models.Model):
    user = models.ManyToManyField(User)

    cover_name = models.CharField(max_length = 50)
    cover_image = models.ImageField(default='default.jpg', upload_to='projects_cvr')

    page_heading = models.CharField(max_length=100)
    page_subheading = models.TextField()

    

    def __str__(self):
        return self.cover_name

class Projects(models.Model):

    thumbnail = models.ImageField(default='default.jpg', upload_to='projects_thumbnails')
    project_title = models.CharField(max_length=100)
    project_summary = models.TextField()
    
    github_link = models.CharField(max_length=500, blank=True,null=True)
    post_link = models.CharField(max_length=500, blank=True,null=True)
    

    def __str__(self):
        return self.project_title

    def save(self, *args, **kwargs):
    
        super().save(*args,**kwargs)


        if self.thumbnail:
            img = Image.open(self.thumbnail)

            if img.width>120 or img.height>120:
                new_size=(120,120)


                img.thumbnail(new_size,Image.ANTIALIAS)

                img.save(self.thumbnail.path)
        