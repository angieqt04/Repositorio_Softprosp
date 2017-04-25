# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Benchmarking', '0006_auto_20170316_2005'),
    ]

    operations = [
        migrations.RenameField(
            model_name='estudio',
            old_name='tutilo',
            new_name='titulo',
        ),
    ]
