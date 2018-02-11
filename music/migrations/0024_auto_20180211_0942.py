# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-02-11 08:42
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0023_auto_20180210_1416'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='creation_date',
            field=models.DateField(blank=True, default=datetime.datetime.now, null=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 2, 11, 9, 42, 29, 523212)),
        ),
    ]
