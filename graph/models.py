from django.db import models
from django.utils import timezone


class Price(models.Model):
    datetime = models.DateTimeField(default=timezone.now)
    xbt = models.DecimalField(max_digits=15, decimal_places=9)
    eth = models.DecimalField(max_digits=15, decimal_places=9)
