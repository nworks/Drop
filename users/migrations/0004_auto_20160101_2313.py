# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-01 23:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20160101_2308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='vacio',
            field=models.CharField(blank=True, max_length=200, unique=True),
        ),
    ]
