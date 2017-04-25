# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Benchmarking', '0008_auto_20170321_1828'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sesion_ideas',
            name='seleccionar_sesion',
        ),
        migrations.RemoveField(
            model_name='sesion_ideas',
            name='usar_sesion',
        ),
    ]
