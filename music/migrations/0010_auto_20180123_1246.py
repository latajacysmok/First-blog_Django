# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-01-23 12:46
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0009_auto_20180123_1245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='publication_date',
            field=models.IntegerField(blank=True, default=1990, null=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 1, 23, 12, 46, 17, 551433)),
        ),
    ]
