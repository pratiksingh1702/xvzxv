from django.contrib import admin
from .models import Content

# Register your models here.
@admin.register(Content)
class Contentadmin(admin.ModelAdmin):
    list_display=['content']