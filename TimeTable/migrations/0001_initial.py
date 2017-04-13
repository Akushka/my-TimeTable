# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DayOfTimeTable',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('day', models.CharField(verbose_name='День недели', max_length=15)),
            ],
            options={
                'db_table': 'DayOfTimeTable',
            },
        ),
        migrations.CreateModel(
            name='TimeTableBase',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('beginLesson', models.TimeField()),
                ('lengthLesson', models.TimeField()),
                ('pauseLesson', models.TimeField()),
                ('timeStr', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'TimeTableBase',
            },
        ),
    ]
