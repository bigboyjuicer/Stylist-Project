from django.db import models


# Create your models here.
class Service(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField
    picture = models.CharField(max_length=256)
    cost = models.IntegerField
