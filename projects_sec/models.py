from django.db import models
from django.urls import reverse

# Create your models here.

class Projects_cover_info(models.Model):

    cover_name = models.CharField(max_length = 50)
    cover_subname = models.CharField(max_length = 150,blank=True, null=True)

    cover_image = models.ImageField(default='default.jpg', upload_to='projects_cvr')

    page_heading = models.CharField(max_length=100)
    page_subheading = models.TextField()

    def __str__(self):
        return self.cover_name

    def get_absolute_url(self):
        return reverse('My-Projects')

    # def save(self, *args, **kwargs):
        
    #     super().save(*args,**kwargs)
                
    #     if self.cover_image:
    #         bg_img = Image.open(self.cover_image)
    #         if bg_img.width > 1920 or bg_img.height > 1280:
    #             new_size=(1920,1280)
    #             bg_img.thumbnail(new_size,Image.ANTIALIAS)
    #             bg_img.save(self.cover_image.path)


class Projects(models.Model):

    thumbnail = models.ImageField(default='default_project.jpg', upload_to='projects_thumbnails')

    project_title = models.CharField(max_length=100)
    project_summary = models.TextField()

    
    github_link = models.CharField(max_length=500, blank=True,null=True)
    post_link = models.CharField(max_length=500, blank=True,null=True)
    

    def __str__(self):
        return self.project_title


    # def save(self, *args, **kwargs):
        
    #     super().save(*args,**kwargs)

    #     if self.thumbnail:
    #         img = Image.open(self.thumbnail)

    #         if img.width>120 or img.height>120:
    #             new_size=(120,120)
    #             img.thumbnail(new_size,Image.ANTIALIAS)
    #             img.save(self.thumbnail.path)


    def get_absolute_url(self):
        return reverse('My-Projects')
