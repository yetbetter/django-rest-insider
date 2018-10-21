from django.contrib.auth.models import User
from django.db import models


class House(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=50)

    class Meta:
        ordering = ['id']