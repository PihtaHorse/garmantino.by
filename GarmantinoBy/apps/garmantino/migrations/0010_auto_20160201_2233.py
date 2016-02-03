# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-01 19:33
from __future__ import unicode_literals

import apps.garmantino.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('garmantino', '0009_auto_20160201_1629'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['status'], 'verbose_name': 'Категория', 'verbose_name_plural': 'Категории'},
        ),
        migrations.AddField(
            model_name='category',
            name='position',
            field=models.PositiveSmallIntegerField(default=1, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='category',
            name='photo',
            field=models.ImageField(default='imgs\\categories\\default-category.jpg', upload_to=apps.garmantino.models.generate_category_image_filename),
        ),
        migrations.AlterField(
            model_name='image',
            name='photo',
            field=models.ImageField(default='imgs\\items\\default-item.jpg', upload_to=apps.garmantino.models.generate_item_image_filename),
        ),
    ]
