# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-09-12 12:29
from __future__ import unicode_literals

import apps.garmantino.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('n', 'Не Используется'), ('y', 'Используется'), ('o', 'Устарела')], default='n', max_length=1, verbose_name='Статус')),
                ('photo', models.ImageField(default='imgs\\categories\\default-category.jpg', upload_to=apps.garmantino.models.Category.generate_filename, verbose_name='Фотография')),
                ('position', models.PositiveSmallIntegerField(blank=True, help_text='Это то, в каком шестиугольнике будет находиться фото.                                                 Оставьте пустым, чтобы значение заполнилось автоматически', verbose_name='Позиция')),
                ('parent_category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='garmantino.Category', verbose_name='Родительская категория')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
                'ordering': ['status'],
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(default='/static/imgs/default-item.jpg', upload_to=apps.garmantino.models.Image.generate_filename, verbose_name='Фото')),
            ],
            options={
                'verbose_name': 'Фото',
                'verbose_name_plural': 'Фотографии',
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название предмета')),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('m', 'В Производстве'), ('y', 'Есть В Наличии'), ('n', 'Нет В Наличии'), ('o', 'Снят С Производства'), ('t', 'Шаблон')], default='m', max_length=1, verbose_name='Статус производства')),
                ('importance', models.CharField(choices=[('a', 'Очень Важный'), ('b', 'Важный'), ('c', 'Не Важный')], default='c', max_length=1, verbose_name='Приоритетность')),
                ('description', models.TextField(blank=True, max_length=300, null=True, verbose_name='Описание')),
                ('category', models.ManyToManyField(help_text='Выбирать мышкой и кнопкой ctrl.                                                Столик может относиться к нескольким категориям!', to='garmantino.Category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Предмет',
                'verbose_name_plural': 'Предметы',
                'ordering': ['pub_date'],
            },
        ),
        migrations.CreateModel(
            name='ItemOnHomePage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('position', models.PositiveSmallIntegerField(blank=True, help_text='Это то, в каком шестиугольнике будет находиться фото.\n                                                 Оставьте пустым, чтобы значение заполнилось автоматически', verbose_name='Позиция')),
                ('item', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='garmantino.Item', verbose_name='Предмет для главной')),
            ],
            options={
                'verbose_name': 'Предмет для главной страницы',
                'verbose_name_plural': 'Предметы для главной страницы',
                'ordering': ['pub_date'],
            },
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Например - цвет', max_length=30, verbose_name='Имя свойства')),
                ('value', models.CharField(blank=True, help_text='Например - красный', max_length=100, verbose_name='Значение свойства')),
                ('order', models.IntegerField(default=1, help_text='В соответствии с этим номером сортируются свойства.                                            Свойства с маленьким порядковым номером - сверху, с большим - снизу', verbose_name='Порядковый номер')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='garmantino.Item')),
            ],
            options={
                'verbose_name': 'Свойство',
                'verbose_name_plural': 'Свойства',
            },
        ),
        migrations.AddField(
            model_name='image',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='garmantino.Item'),
        ),
    ]
