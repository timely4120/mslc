# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-11 20:37
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0009_auto_20180411_1314'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Department', models.CharField(max_length=4)),
                ('Number', models.CharField(max_length=4)),
                ('Name', models.CharField(max_length=200)),
                ('SubjectID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subjectCourse', to='schedule.Subject')),
                ('TutorForCourse', models.ManyToManyField(to='schedule.Tutor')),
            ],
        ),
        migrations.AlterField(
            model_name='shift',
            name='EndTime',
            field=models.TimeField(choices=[(datetime.time(8, 30), '08:30'), (datetime.time(9, 0), '09:00'), (datetime.time(9, 30), '09:30'), (datetime.time(10, 0), '10:00'), (datetime.time(10, 30), '10:30'), (datetime.time(11, 0), '11:00'), (datetime.time(11, 30), '11:30'), (datetime.time(12, 0), '12:00'), (datetime.time(12, 30), '12:30'), (datetime.time(13, 0), '13:00'), (datetime.time(13, 30), '13:30'), (datetime.time(14, 0), '14:00'), (datetime.time(14, 30), '14:30'), (datetime.time(15, 0), '15:00'), (datetime.time(15, 30), '15:30'), (datetime.time(16, 0), '16:00'), (datetime.time(16, 30), '16:30'), (datetime.time(17, 0), '17:00'), (datetime.time(17, 30), '17:30'), (datetime.time(18, 0), '18:00'), (datetime.time(18, 30), '18:30'), (datetime.time(19, 0), '19:00'), (datetime.time(19, 30), '19:30'), (datetime.time(20, 0), '20:00'), (datetime.time(20, 30), '20:30'), (datetime.time(21, 0), '21:00'), (datetime.time(21, 30), '21:30'), (datetime.time(22, 0), '22:00'), (datetime.time(22, 30), '22:30'), (datetime.time(23, 0), '23:00'), (datetime.time(23, 30), '23:30')]),
        ),
        migrations.AlterField(
            model_name='shift',
            name='StartTime',
            field=models.TimeField(choices=[(datetime.time(8, 30), '08:30'), (datetime.time(9, 0), '09:00'), (datetime.time(9, 30), '09:30'), (datetime.time(10, 0), '10:00'), (datetime.time(10, 30), '10:30'), (datetime.time(11, 0), '11:00'), (datetime.time(11, 30), '11:30'), (datetime.time(12, 0), '12:00'), (datetime.time(12, 30), '12:30'), (datetime.time(13, 0), '13:00'), (datetime.time(13, 30), '13:30'), (datetime.time(14, 0), '14:00'), (datetime.time(14, 30), '14:30'), (datetime.time(15, 0), '15:00'), (datetime.time(15, 30), '15:30'), (datetime.time(16, 0), '16:00'), (datetime.time(16, 30), '16:30'), (datetime.time(17, 0), '17:00'), (datetime.time(17, 30), '17:30'), (datetime.time(18, 0), '18:00'), (datetime.time(18, 30), '18:30'), (datetime.time(19, 0), '19:00'), (datetime.time(19, 30), '19:30'), (datetime.time(20, 0), '20:00'), (datetime.time(20, 30), '20:30'), (datetime.time(21, 0), '21:00'), (datetime.time(21, 30), '21:30'), (datetime.time(22, 0), '22:00'), (datetime.time(22, 30), '22:30'), (datetime.time(23, 0), '23:00'), (datetime.time(23, 30), '23:30')]),
        ),
    ]