from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class HomePage(models.Model):
    user = models.ManyToManyField(User)

    heading = models.CharField(max_length=50)
    Summary = models.TextField()
    link = models.CharField(max_length=100)

    def __str__(self):
        return self.heading





