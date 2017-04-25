# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Benchmarking', '0004_auto_20170315_2010'),
    ]

    operations = [
        migrations.CreateModel(
            name='Benchmarking',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codigo', models.PositiveIntegerField(default=1)),
                ('tutilo', models.CharField(max_length=100)),
                ('tematica', models.CharField(max_length=100)),
                ('analista_externo', models.ManyToManyField(related_name='bench_analista_externo_set', verbose_name=b'Analista_externo', to=settings.AUTH_USER_MODEL)),
                ('equipo_expertos', models.ManyToManyField(related_name='bench_expertos_set', verbose_name=b'Expertos', to=settings.AUTH_USER_MODEL)),
                ('moderador', models.ManyToManyField(related_name='bench_moderador_set', verbose_name=b'Moderador', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='actividad',
            name='analista_externo',
        ),
        migrations.RemoveField(
            model_name='actividad',
            name='equipo_expertos',
        ),
        migrations.RemoveField(
            model_name='actividad',
            name='moderador',
        ),
    ]
