# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-25 02:58
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('graph', '0005_auto_20170624_1712'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='price',
            name='published_date',
        ),
    ]