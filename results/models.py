from enum import Enum

from django.db import models

# Create your models here

class Result(models.Model):
    id = models.AutoField(primary_key=True)
    created_by = models.CharField(max_length=255)
    created_on = models.DateTimeField(max_length=255)
    homeranking = models.JSONField()
    awayranking = models.JSONField()
    logoranking = models.JSONField()