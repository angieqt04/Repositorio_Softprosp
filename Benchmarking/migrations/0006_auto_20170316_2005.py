# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Benchmarking', '0005_auto_20170316_1415'),
    ]

    operations = [
        migrations.CreateModel(
            name='Estudio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codigo', models.PositiveIntegerField(default=1)),
                ('tutilo', models.CharField(max_length=100)),
                ('tematica', models.CharField(max_length=100)),
                ('analista_externo', models.ManyToManyField(related_name='bench_analista_externo_set', verbose_name=b'Analista_externo', to=settings.AUTH_USER_MODEL)),
                ('equipo_expertos', models.ManyToManyField(related_name='bench_expertos_set', verbose_name=b'Expertos', to=settings.AUTH_USER_MODEL)),
                ('moderador', models.ManyToManyField(related_name='bench_moderador_set', verbose_name=b'Moderador', to=settings.AUTH_USER_MODEL)),
                ('organizacion', models.OneToOneField(related_name='bench_organizacion_set', verbose_name=b'Organizacion_bench', to='Benchmarking.Organizacion')),
            ],
        ),
        migrations.RemoveField(
            model_name='benchmarking',
            name='analista_externo',
        ),
        migrations.RemoveField(
            model_name='benchmarking',
            name='equipo_expertos',
        ),
        migrations.RemoveField(
            model_name='benchmarking',
            name='moderador',
        ),
        migrations.AlterField(
            model_name='actividad',
            name='recursos',
            field=models.BigIntegerField(),
        ),
        migrations.DeleteModel(
            name='Benchmarking',
        ),
    ]
