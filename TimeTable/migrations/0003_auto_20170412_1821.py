# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TimeTable', '0002_lessoninday'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timetablebase',
            name='lengthLesson',
            field=models.CharField(max_length=20),
        ),
    ]
