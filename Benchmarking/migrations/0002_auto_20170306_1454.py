# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Benchmarking', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lluvia_de_ideas',
            name='equipo_expertos',
            field=models.ManyToManyField(related_name='grupo_expertos', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='lluvia_de_ideas',
            name='moderador',
            field=models.ManyToManyField(related_name='moderador', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='actividad',
            name='analista_externo',
            field=models.ManyToManyField(related_name='analista_externo', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='actividad',
            name='equipo_expertos',
            field=models.ManyToManyField(related_name='equipo_expertos', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='actividad',
            name='moderador',
            field=models.ManyToManyField(related_name='coordinador', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='entrevista',
            name='equipo_expertos',
            field=models.ManyToManyField(related_name='expertos', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='entrevista',
            name='organizacion',
            field=models.OneToOneField(to='Benchmarking.Organizacion'),
        ),
    ]
