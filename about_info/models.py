from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from ckeditor_uploader.fields import RichTextUploadingField
from django.urls import reverse
from PIL import Image

# Create your models here.

class AboutMe(models.Model):

    cover_image = models.ImageField(default='default_about_cvr.jpg', upload_to='about_cvr')

    cover_name = models.CharField(max_length=50)
    micro_greeting_1 = models.CharField(max_length=50, blank=True,null=True)
    micro_greeting_2 = models.CharField(max_length=50, blank=True,null=True)
    short_intro = models.CharField(max_length=50, blank=True,null=True)

    greeting_heading = models.CharField(max_length=50)
    greeting_subheading = models.CharField(max_length=50, blank=True,null=True)

    self_intro = RichTextUploadingField()
    fairwell_words = RichTextUploadingField()

    def __str__(self):
        return self.cover_name
    
    def get_absolute_url(self):
        return reverse('About-Me')

    # def save(self, *args, **kwargs):
        
    #     super().save(*args,**kwargs)
       
    #     if self.cover_image:
    #         bg_img = Image.open(self.cover_image)
    #         if bg_img.width > 1920 or bg_img.height > 1280:
    #             new_size=(1920,1280)
    #             bg_img.thumbnail(new_size,Image.ANTIALIAS)
    #             bg_img.save(self.cover_image.path)
