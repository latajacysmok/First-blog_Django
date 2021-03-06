# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-02-12 11:34
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0024_auto_20180211_0942'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 2, 12, 12, 34, 34, 196399)),
        ),
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(default='/music/static/music/images/default.jpg', upload_to='music/static/music/images/'),
        ),
    ]
