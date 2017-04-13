# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TimeTable', '0006_auto_20170412_1829'),
    ]

    operations = [
        migrations.AddField(
            model_name='timetablebase',
            name='count',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
