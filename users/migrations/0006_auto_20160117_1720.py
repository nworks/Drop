# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-17 17:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20160101_2320'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_pic', models.ImageField(upload_to='userpic/')),
                ('username', models.CharField(blank=True, max_length=100, unique=True)),
                ('Password', models.CharField(max_length=50, null=True)),
                ('first_name', models.CharField(blank=True, max_length=25)),
                ('last_name', models.CharField(blank=True, max_length=25)),
                ('Email', models.EmailField(max_length=254, unique=True, verbose_name='Email')),
            ],
        ),
        migrations.AlterField(
            model_name='cliente',
            name='Empthy',
            field=models.EmailField(max_length=254, unique=True, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='direccion',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='fechaintro',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='vacio',
            field=models.CharField(blank=True, max_length=15, unique=True, verbose_name='Password'),
        ),
    ]
