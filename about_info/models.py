from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.
class AboutMe(models.Model):
    user = models.ManyToManyField(User)

    cover_name = models.CharField(max_length=50)

    micro_greeting_1 = models.CharField(max_length=50, blank=True,null=True)
    micro_greeting_2 = models.CharField(max_length=50, blank=True,null=True)
    short_intro = models.CharField(max_length=50, blank=True,null=True)
    greeting_heading = models.CharField(max_length=50)
    greeting_subheading = models.CharField(max_length=50, blank=True,null=True)
    self_intro = models.TextField()
    fairwell_words = models.TextField()

    def __str__(self):
        return self.cover_name
