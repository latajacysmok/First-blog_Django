# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-01-19 12:14
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0004_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='pub_date',
        ),
        migrations.AddField(
            model_name='comment',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 1, 19, 13, 14, 57, 719945)),
        ),
    ]