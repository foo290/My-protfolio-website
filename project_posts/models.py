from django.db import models
from projects_sec.models import Projects
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.

class P_Post(models.Model):
    project = models.OneToOneField(Projects,on_delete=models.CASCADE)
    project_summary = RichTextUploadingField(default='Post Coming Soon!')

    def __str__(self):
        return str(self.project)

    def get_absolute_url(self):
        return reverse('Projects-Detail', kwargs={'pk': self.pk})