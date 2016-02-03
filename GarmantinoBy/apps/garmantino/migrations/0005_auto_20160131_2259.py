# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-31 19:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('garmantino', '0004_auto_20160131_1719'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='parent_category',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='garmantino.Category'),
        ),
        migrations.AlterField(
            model_name='category',
            name='status',
            field=models.CharField(choices=[('n', 'Не Используется'), ('y', 'Используется'), ('o', 'Устарела')], default='n', max_length=1),
        ),
    ]