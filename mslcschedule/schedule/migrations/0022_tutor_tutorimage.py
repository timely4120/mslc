# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-05-01 17:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0021_auto_20180501_0830'),
    ]

    operations = [
        migrations.AddField(
            model_name='tutor',
            name='TutorImage',
            field=models.ImageField(default='static/images/profiles/empty-profile.png', upload_to='static/images/profiles'),
        ),
    ]
