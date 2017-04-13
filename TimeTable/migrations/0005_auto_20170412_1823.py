# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TimeTable', '0004_auto_20170412_1822'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timetablebase',
            name='beginLesson',
            field=models.TimeField(),
        ),
    ]
