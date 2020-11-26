from django.contrib import admin

# Register your models here.
from .models import Projects,Projects_cover_info

admin.site.register(Projects)
admin.site.register(Projects_cover_info)
