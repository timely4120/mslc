# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-18 17:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0013_auto_20180411_1604'),
    ]

    operations = [
        migrations.AddField(
            model_name='tutor',
            name='following',
            field=models.ManyToManyField(related_name='followers', through='schedule.Course', to='schedule.Tutor'),
        ),
    ]
