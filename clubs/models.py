from django.db import models

# Create your models here.
class Club(models.Model):
    name = models.CharField(max_length=255, primary_key=True)
    logo = models.CharField(max_length=255)
    homekit = models.CharField(max_length=255)
    awaykit = models.CharField(max_length=255)
    specialkit = models.CharField(max_length=255)