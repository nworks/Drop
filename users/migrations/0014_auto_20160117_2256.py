# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-17 22:56
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_usuarioprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuarioprofile',
            name='idfield',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AlterField(
            model_name='usuarioprofile',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
