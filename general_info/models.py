from django.db import models
from django.contrib.auth.models import User
from PIL import Image


# Create your models here.

class PrimaryUser(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE)

    home_bg = models.ImageField(default='default.jpg', upload_to='home_bg')

    name = models.CharField(max_length=50)
    fancy_name = models.CharField(max_length=50)
    bio = models.TextField()
    status = models.TextField()
    pfp = models.ImageField(default='default.jpg', upload_to='profile_pics')


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
    
    def save(self, *args, **kwargs):

        super().save(*args,**kwargs)


        if self.pfp:
            img = Image.open(self.pfp)
            if img.width !=img.height:
                new_w,new_h = (img.width, img.width)
                left = (img.width-new_w)//2
                top = (img.height-new_h)//2
                right = (img.width+new_w)//2
                bottom = (img.height+new_h)//2


                img = img.crop((left, top, right, bottom))

                img.save(self.pfp.path)

        # super(PrimaryUser, self).save(*args, **kwargs)