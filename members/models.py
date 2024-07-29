from django.db import models

class Member(models.Model):
    appleId = models.CharField(max_length=255, primary_key=True)
    email = models.CharField(max_length=255)
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)