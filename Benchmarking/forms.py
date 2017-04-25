# coding: utf-8
from django import forms
from Benchmarking.models import Actividad, Organizacion, Estudio, Sesion_ideas, Idea, Conclusion

class ActividadForm(forms.ModelForm):

    class Meta:
        model = Actividad

        fields = (
            'nombre_actividad',
            'objetivos_iniciales',
            'organizacion_objetivo',
           # 'calendario_previsto',
            'recursos',
            #'proceso',
            'efecto',
        )

        labels = {
            'nombre_actividad': 'Nombre de la actividad',
            'objetivos_iniciales': 'Objetivos iniciales',
            'organizacion_objetivo': u'Nombre de la organización objetivo',
            #'calendario_previsto': 'Calendario previsto',
            'recursos': 'Recurso',
            #'proceso': 'Proceso',
            'efecto': 'Efecto',
            'equipo_expertos': 'Equipo de expertos',
            'moderador': 'Moderador',
            'analista_externo': 'Analista externo',
        }

        widgets = {
            'nombre_actividad': forms.TextInput(attrs={'class': 'form-control'}),
            'objetivos_iniciales': forms.Textarea(attrs={'class': 'form-control', 'rows':'3', 'placeholder': 'Ingresar los objetivos iniciales del estudio'}),
            'organizacion_objetivo': forms.TextInput(attrs={'class': 'form-control'}),
            #'calendario_previsto': forms.FileInput(attrs={'class': 'form-control'}),
            'recursos': forms.TextInput(attrs={'class': 'form-control'}),
            #'proceso': forms.FileInput(attrs={'class': 'form-control'}),
            'efecto': forms.TextInput(attrs={'class': 'form-control'}),
        }

        exclude =(
            'calendario_previsto',
            'proceso'
        )

class OrganizacionForm(forms.ModelForm):

    class Meta:
        model = Organizacion

        fields = (
            'nombre_organizacion',
            'pais',
            'tipo_organizacion',
            'directivo_organizacion',
        )

        labels = {
            'nombre_organizacion': 'Nombre de la organización',
            'pais': 'País',
            'tipo_organizacion': 'Tipo de Organización',
            'directivo_organizacion': 'Directivo de la organización',
        }

        widgets = {
            'nombre_organizacion': forms.TextInput(attrs={'class':'form-control'}),
            'pais': forms.TextInput(attrs={'class':'form-control'}),
            'tipo_organizacion': forms.Select(attrs={'class':'form-control'}),
            'directivo_organizacion':forms.Select(attrs={'class':'form-control'}),

        }

class EstudioForm(forms.ModelForm):

    class Meta:
        model = Estudio

        fields = (
            'codigo',
            'titulo',
            'tematica',
            'equipo_expertos',
            'moderador',
            'analista_externo',
        )

        labels = {
            'codigo': 'Codigo',
            'titulo': 'Título',
            'tematica': 'Tematica',
            'equipo_expertos': 'Equipo de expertos',
            'moderador': 'Moderador',
            'analista_externo': 'Analista externo',
        }

        widgets = {
            'codigo': forms.TextInput(attrs={'class': 'form-control'}),
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'tematica': forms.TextInput(attrs={'class':'form-control'}),
            'equipo_expertos': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'moderador': forms.SelectMultiple(attrs={'class':'form-control'}),
            'analista_externo': forms.SelectMultiple(attrs={'class':'form-control'}),
        }

class SesionForm(forms.ModelForm):

    class Meta:

        model = Sesion_ideas

        fields = (
            'codigo_sesion',
            'fecha_inicial',
            'fecha_final',
            'permitir_ideas',
            'estado',
        )

        labels= {
            'codigo_sesion': 'Código',
            'fecha_inicial': 'Fecha Inicial',
            'fecha_final': 'Fecha Final',
            'permitir_ideas': 'Permitir ideas',
            'estado': 'Estado',
        }

        widgets = {
            'codigo_sesion': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_inicial': forms.DateInput(attrs={'class': 'form-control'}),
            'fecha_final': forms.DateInput(attrs={'class': 'form-control'}),
            'permitir_ideas':forms.CheckboxInput(),
            'estado': forms.CheckboxInput()
        }

class IdeaForm(forms.ModelForm):

    class Meta:
        model = Idea

        fields = (
            'definicion_idea',
            'argumento',
        )

        labels = {
            'definicion_idea': 'Factor',
            'argumento': 'Descripción',
        }

        widgets = {
            'definicion_idea': forms.TextInput(attrs={'class': 'form-control'}),
            'argumento': forms.Textarea(attrs={'class': 'form-control', 'rows':'3', 'placeholder': 'Describir factor'}),
        }

class factor_concluido(forms.ModelForm):

    class Meta:
        model = Conclusion

        fields = (
            'nombre_corto',
            'titulo',
            'descripcion',
            'ideas',
        )

        widgets = {
            'nombre_corto': forms.TextInput(attrs={'class': 'form-control'}),
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows':'3', 'placeholder': 'Justificar conclusión'}),
            'ideas': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }

