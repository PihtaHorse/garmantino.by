# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-31 14:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('garmantino', '0002_auto_20160131_1521'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='status',
            field=models.CharField(choices=[('d', 'Черновик'), ('p', 'Опубликован'), ('o', 'Устарел')], default='d', max_length=1),
        ),
        migrations.AddField(
            model_name='item',
            name='status',
            field=models.CharField(choices=[('d', 'Черновик'), ('p', 'Опубликован'), ('o', 'Устарел')], default='d', max_length=1),
        ),
    ]
