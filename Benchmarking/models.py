# coding: utf-8
from django.db import models
from django.utils.timezone import now
from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User

# Create your models here.
class Organizacion(models.Model):

    CLASIFICACION_ORG = (
        ('1', 'Extractiva'),
        ('2', u'Agrícola'),
        ('3', 'Fabril'),
        ('4', 'Comercial'),
        ('5', 'Sanitaria'),
        ('6', 'Instructora'),
        ('7', 'Social'),
        ('8', 'Servicios'),
    )
    nombre_organizacion = models.CharField(max_length=120)
    pais = models.CharField(max_length= 20)
    tipo_organizacion = models.CharField(max_length=1, choices=CLASIFICACION_ORG)
    directivo_organizacion = models.OneToOneField(User, primary_key=True)

    class Meta:
        verbose_name = 'Organizacion'
        verbose_name_plural = 'Organizaciones'

class Publicacion(models.Model):
    asunto = models.CharField(max_length=120)
    mensaje = models.TextField()
    archivo = models.FileField()
    fecha_actual = models.DateTimeField()
    usuario = models.OneToOneField(User)

    class Meta:
        verbose_name = 'Publicacion'
        verbose_name_plural = 'Publicaciones'

class Actividad(models.Model):
    nombre_actividad = models.CharField(max_length=30)
    objetivos_iniciales = models.TextField()
    organizacion_objetivo = models.CharField(max_length=120)
    calendario_previsto = models.FileField()
    recursos = models.PositiveIntegerField()
    proceso = models.FileField()
    efecto = models.CharField(max_length=20)
    equipo_expertos = models.ManyToManyField(User, related_name='expertos')
    moderador = models.ManyToManyField(User, related_name='moderador')
    analista_externo = models.ManyToManyField(User, related_name='analista_externo')

    class Meta:
        verbose_name = 'Actividad'
        verbose_name_plural = 'Actividades'

class Lluvia_de_ideas(models.Model):
    reglas = models.TextField()
    titulo = models.CharField(max_length=50)
    equipo_expertos = models.ManyToManyField(User, related_name = 'expertos')
    moderador = models.ManyToManyField(User, related_name = 'moderador')

    class Meta:
        verbose_name = 'Lluvia de ideas'
        verbose_name_plural = 'Lluvias de ideas'

class Entrevista(models.Model):
    cargo_invitado = models.CharField(max_length=30)
    email_invitado = models.EmailField()
    objetivo_entrevista = models.TextField()
    preguntas = models.ForeignKey(Lluvia_de_ideas)
    organizacion = models.OneToOneField(Organizacion)
    equipo_expertos = models.ManyToManyField(User, related_name = 'expertos')

    class Meta:
        verbose_name = 'Entrevista'
        verbose_name_plural = 'Entrevistas'

class Sesion_ideas(models.Model):
    codigo_sesion = models.PositiveIntegerField()
    fecha_actual =  models.DateTimeField(default=now)
    fecha_inicial = models.DateField(default=now)
    fecha_final = models.DateField(default=now)
    permitir_ideas = models.BooleanField(default=False, help_text='Permitir la cracion de ideas')
    estado = models.BooleanField(default=True, help_text='Permitir la votación de ideas')
    lluvia_de_ideas = models.ForeignKey('Lluvia_de_ideas', verbose_name='Lluvia de ideas')
    usar_sesion = models.ForeignKey('Sesion_ideas', blank=True, null=True, verbose_name='Sesion Padre')
    seleccionar_sesion = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'Sesion de ideas'
        verbose_name_plural = 'Sesiones de ideas'
        unique_together = ('codigo_sesion', 'lluvia_de_ideas')
        ordering = ('lluvia_de_ideas', 'codigo_sesion')

class Idea(models.Model):
    codigo_idea = models.CharField(max_length=5)
    definicion_idea = models.CharField(max_length=20)
    argumento = models.TextField()
    dependencia = models.CharField(max_length=20)
    lluvia_de_idea = models.ForeignKey(Lluvia_de_ideas)

    class Meta:
        verbose_name = 'Idea'
        verbose_name_plural = 'Ideas'

class Diagrama_de_causa_efecto(models.Model):

    efeecto = models.ForeignKey(Actividad)
    lluvia_de_idea = models.ForeignKey(Lluvia_de_ideas)
    factor_clave = models.CharField(max_length=20)

    class Meta:
        verbose_name = 'Diagrama de causa y efecto'
        verbose_name_plural = 'Diagramas de causa y efecto'

class Diagrama_de_pareto(models.Model):
    frecuencia_acumulada = models.PositiveIntegerField()
    frecuencia_porcentual = models.PositiveIntegerField()
    frecuencia_porcentual_acumulada = models.PositiveIntegerField()

    class Meta:
        verbose_name = 'Diagrama de pareto'
        verbose_name_plural = 'Diagramas de pareto'

class Punto_de_medida(models.Model):
    factor_clave = models.OneToOneField(Idea, primary_key=True)
    frecuencia = models.PositiveIntegerField()
    argumento = models.TextField()
    Diagrama_de_pareto = models.ForeignKey(Diagrama_de_pareto)

    class Meta:
        verbose_name = 'Punto de mdedida'
        verbose_name_plural = 'Puntos de medidas'












