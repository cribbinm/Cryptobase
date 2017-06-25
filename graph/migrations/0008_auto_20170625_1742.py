# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-25 05:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('graph', '0007_price_entry'),
    ]

    operations = [
        migrations.AlterField(
            model_name='price',
            name='entry',
            field=models.IntegerField(max_length=4),
        ),
        migrations.AlterField(
            model_name='price',
            name='eth',
            field=models.IntegerField(max_length=200),
        ),
        migrations.AlterField(
            model_name='price',
            name='xbt',
            field=models.IntegerField(max_length=200),
        ),
    ]