# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-02-01 04:07
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0021_auto_20180130_1808'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='album_logo',
            field=models.ImageField(blank=True, default='D:/Projekty/blog1/First-blog_Django/music/static/music/images/background.jpg', null=True, upload_to='music/static/music/images/'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 2, 1, 5, 7, 18, 901538)),
        ),
    ]