from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Nav_cards(models.Model):

    heading = models.CharField(max_length=50)
    Summary = models.TextField()
    link = models.CharField(max_length=100)

    def __str__(self):
        return self.heading

    def get_absolute_url(self):
        return reverse('Home-Landing')






