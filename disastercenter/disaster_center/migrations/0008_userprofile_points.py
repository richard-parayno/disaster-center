# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-27 09:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('disaster_center', '0007_auto_20160827_1701'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='points',
            field=models.IntegerField(default=0),
        ),
    ]
