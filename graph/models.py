from django.db import models
# from django.utils import timezone
import time


class Price(models.Model):
    # published_date = models.DateTimeField(default=timezone.now)
    # xbt = models.DecimalField(max_digits=15, decimal_places=9)
    # eth = models.DecimalField(max_digits=15, decimal_places=9)
    # timestamp = int(time.time())
    entry = models.FloatField()
    xbt = models.FloatField()
    eth = models.FloatField()

    # def __str__(self):
    #     return self.xbt