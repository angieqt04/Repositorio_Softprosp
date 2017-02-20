

# Create your models here.
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Usuario(models.Model):
	id_usuario = models.BigIntegerField()
	nombre_usuario = models.CharField(max_length=120, blank=True, null=True)
	email = models.EmailField()
	tipo_usuario = models.IntegerField()

	def __unicode__(self):
		return self.id_usuario