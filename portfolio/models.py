from django.db import models


# Create your models here.
class Portfolio(models.Model):
    title = models.CharField(max_length=256)
    cover_picture = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return self.title


class Picture(models.Model):
    picture = models.ImageField(upload_to='images/', null=True, blank=True)
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
