# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-27 23:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog1', '0005_post_autor'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='picturep',
            field=models.ImageField(blank=True, upload_to='picturep/'),
        ),
    ]