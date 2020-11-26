from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Skills(models.Model):

    heading = models.CharField(max_length=50)
    items = models.TextField()

    def __str__(self):
        return self.heading

    def get_absolute_url(self):
        return reverse('Home-Landing')
