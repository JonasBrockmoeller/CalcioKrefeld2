from django.db import models

# Create your models here.
class Prognosis(models.Model):
    id = models.AutoField(primary_key=True)
    created_by = models.CharField(max_length=255)
    created_on = models.DateTimeField(max_length=255)
    prognosis_champion = models.TextField()
    prognosis_topscorer = models.TextField()
    prognosis_trainer_fired = models.TextField()
    prognosis_surprise = models.TextField()
    prognosis_disappointment = models.TextField()
    prognosis_hottake = models.TextField()