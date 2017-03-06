from django.contrib import admin

# Register your models here.
from Benchmarking.models import Organizacion
from Benchmarking.models import Publicacion
from Benchmarking.models import Entrevista
from Benchmarking.models import Actividad
from Benchmarking.models import Sesion_ideas
from Benchmarking.models import Lluvia_de_ideas
from Benchmarking.models import Idea
from Benchmarking.models import Diagrama_de_causa_efecto
from Benchmarking.models import Punto_de_medida
from Benchmarking.models import Diagrama_de_pareto

admin.site.register(Organizacion)
admin.site.register(Publicacion)
admin.site.register(Entrevista)
admin.site.register(Actividad)
admin.site.register(Sesion_ideas)
admin.site.register(Lluvia_de_ideas)
admin.site.register(Idea)
admin.site.register(Diagrama_de_causa_efecto)
admin.site.register(Punto_de_medida)
admin.site.register(Diagrama_de_pareto)