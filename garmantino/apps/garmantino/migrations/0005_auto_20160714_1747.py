# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-07-14 14:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('garmantino', '0004_auto_20160714_1735'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='description',
            field=models.TextField(blank=True, max_length=300, null=True, verbose_name='Описание'),
        ),
    ]
