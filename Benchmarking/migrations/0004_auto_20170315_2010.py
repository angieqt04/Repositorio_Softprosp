# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Benchmarking', '0003_auto_20170308_1626'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actividad',
            name='efecto',
            field=models.CharField(max_length=120),
        ),
        migrations.AlterField(
            model_name='actividad',
            name='nombre_actividad',
            field=models.CharField(max_length=120),
        ),
    ]
