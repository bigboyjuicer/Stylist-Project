from django.db import models
from users.models import User
from services.models import Service


# Create your models here.
class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    services = models.ForeignKey(Service, on_delete=models.CASCADE)
    comment = models.TextField
