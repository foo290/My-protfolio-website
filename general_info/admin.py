from django.contrib import admin

# Register your models here.

from .models import PrimaryUser
admin.site.register(PrimaryUser)