# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-27 14:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_task', '0004_auto_20170727_0229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campaign',
            name='name',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='channel',
            name='name',
            field=models.CharField(max_length=15),
        ),
    ]