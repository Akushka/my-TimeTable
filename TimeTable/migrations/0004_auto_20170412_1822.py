# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TimeTable', '0003_auto_20170412_1821'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timetablebase',
            name='beginLesson',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='timetablebase',
            name='pauseLesson',
            field=models.CharField(max_length=20),
        ),
    ]
