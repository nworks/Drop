# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-17 20:18
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_auto_20160117_2016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
