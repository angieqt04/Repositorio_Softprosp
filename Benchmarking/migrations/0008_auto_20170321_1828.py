# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Benchmarking', '0007_auto_20170316_2027'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sesion_ideas',
            options={'verbose_name': 'Sesion de ideas', 'verbose_name_plural': 'Sesiones de ideas'},
        ),
        migrations.AlterUniqueTogether(
            name='sesion_ideas',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='sesion_ideas',
            name='fecha_actual',
        ),
        migrations.RemoveField(
            model_name='sesion_ideas',
            name='lluvia_de_ideas',
        ),
    ]
