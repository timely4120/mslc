# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-19 23:48
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0016_auto_20180419_1844'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='availability',
            options={'ordering': ['Day', 'StartTime']},
        ),
    ]