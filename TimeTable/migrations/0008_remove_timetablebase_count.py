# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TimeTable', '0007_timetablebase_count'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='timetablebase',
            name='count',
        ),
    ]
