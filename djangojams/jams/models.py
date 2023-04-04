from django.db import models

# Create your models here.
class song(models.model):
    name = models.CharField(max_length=500)
    duration = models.Duration()

