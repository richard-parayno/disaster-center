# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-27 06:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('disaster_center', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='exp',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
