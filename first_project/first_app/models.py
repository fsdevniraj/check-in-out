from django.db import models

# Create your models here.

class Items(models.Model):
    name = models.CharField(max_length=264,unique=True)
    status = models.CharField(max_length=264)
