from django.db import models

# Create your models here.
class Content(models.Model):
    content=models.CharField(default="student",max_length=99,null=False)