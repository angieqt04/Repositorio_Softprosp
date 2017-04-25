# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Benchmarking', '0002_auto_20170306_1454'),
    ]

    operations = [
        migrations.RenameField(
            model_name='diagrama_de_causa_efecto',
            old_name='efeecto',
            new_name='efecto',
        ),
    ]
