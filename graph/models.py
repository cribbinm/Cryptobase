from django.db import models
from django.utils import timezone


class Price(models.Model):
    published_date = models.DateTimeField(default=timezone.now)
    # xbt = models.DecimalField(max_digits=15, decimal_places=9)
    # eth = models.DecimalField(max_digits=15, decimal_places=9)
    xbt = models.CharField(max_length=200)
    eth = models.CharField(max_length=200)

    def __str__(self):
        return self.xbt