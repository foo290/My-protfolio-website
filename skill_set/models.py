from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Skills(models.Model):
    user = models.ManyToManyField(User)

    heading = models.CharField(max_length=50)
    items = models.TextField()

    def __str__(self):
        return self.heading