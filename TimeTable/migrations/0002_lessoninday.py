# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TimeTable', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LessonInDay',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('nameLesson', models.CharField(max_length=20)),
                ('lesson_id', models.ForeignKey(to='TimeTable.DayOfTimeTable')),
            ],
            options={
                'db_table': 'LessonInDay',
            },
        ),
    ]
