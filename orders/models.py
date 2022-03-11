from django.db import models
from services.models import Service
from users.models import User


class Order(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField
    comment = models.TextField
