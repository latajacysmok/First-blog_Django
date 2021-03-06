# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-01-26 17:10
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0018_auto_20180123_1855'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='edit_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='album',
            name='album_logo',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='comment',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 1, 26, 18, 10, 42, 399633)),
        ),
    ]
