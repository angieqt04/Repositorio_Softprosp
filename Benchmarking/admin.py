from django.contrib import admin

# Register your models here.
from Benchmarking.models import Organizacion, Publicacion, Entrevista, Actividad, Sesion_ideas, Lluvia_de_ideas, Idea,\
    Diagrama_de_causa_efecto, Punto_de_medida, Diagrama_de_pareto, Estudio, Conclusion

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
admin.site.register(Estudio)
admin.site.register(Conclusion)