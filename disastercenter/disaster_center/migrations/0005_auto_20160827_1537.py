# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-27 07:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('disaster_center', '0004_auto_20160827_1528'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='dateTimeEnd',
            field=models.DateField(default='00/00/00'),
        ),
    ]
