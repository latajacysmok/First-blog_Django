# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-01-23 18:45
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0012_auto_20180123_1843'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='author',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 1, 23, 18, 45, 28, 666735)),
        ),
    ]
