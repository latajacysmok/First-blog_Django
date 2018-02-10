# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-02-02 03:36
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0024_auto_20180202_0427'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 2, 2, 4, 36, 12, 451806)),
        ),
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(default='music/static/music/images/background.jpg', upload_to='music/static/music/images'),
        ),
    ]