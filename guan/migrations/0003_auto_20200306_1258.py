# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-03-06 12:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guan', '0002_auto_20200306_1254'),
    ]

    operations = [
        migrations.CreateModel(
            name='GuanType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('created_time', models.DateTimeField()),
                ('updated_time', models.DateTimeField()),
            ],
            options={
                'db_table': 'guan_type',
            },
        ),
        migrations.RemoveField(
            model_name='book',
            name='authors',
        ),
        migrations.RemoveField(
            model_name='book',
            name='publisher',
        ),
        migrations.DeleteModel(
            name='Author',
        ),
        migrations.DeleteModel(
            name='Book',
        ),
        migrations.DeleteModel(
            name='Publisher',
        ),
    ]