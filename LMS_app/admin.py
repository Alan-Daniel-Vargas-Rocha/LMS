from django.contrib import admin
from .models import (
    Usuario, Rol, UsuarioRol, Categoria, Curso, Modulo, Inscripcion,
    Leccion, ProgresoLeccion, Evaluacion, Pregunta, OpcionRespuesta,
    IntentoEvaluacion, RespuestaEstudiante, Calificacion, Certificado,
    ComentarioForo, Pago,
)

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('id_usuario', 'nombre', 'apellido', 'email', 'activo', 'fecha_registro')
    search_fields = ('nombre', 'apellido', 'email')
    list_filter = ('activo',)

@admin.register(Rol)
class RolAdmin(admin.ModelAdmin):
    list_display = ('id_rol', 'nombre')
    search_fields = ('nombre',)

@admin.register(UsuarioRol)
class UsuarioRolAdmin(admin.ModelAdmin):
    list_display = ('id_usuario_rol', 'id_usuario', 'id_rol', 'fecha_asignacion')

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id_categoria', 'nombre', 'creado')
    search_fields = ('nombre',)

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('id_curso', 'titulo', 'id_categoria', 'id_instructor', 'nivel', 'precio', 'publicado')
    list_filter = ('publicado', 'nivel', 'id_categoria')
    search_fields = ('titulo', 'slug')
    prepopulated_fields = {'slug': ('titulo',)}

@admin.register(Modulo)
class ModuloAdmin(admin.ModelAdmin):
    list_display = ('id_modulo', 'titulo', 'id_curso', 'orden')
    list_filter = ('id_curso',)

@admin.register(Inscripcion)
class InscripcionAdmin(admin.ModelAdmin):
    list_display = ('id_inscripcion', 'id_usuario', 'id_curso', 'estado', 'progreso_porcentaje', 'fecha_inscripcion')
    list_filter = ('estado',)

@admin.register(Leccion)
class LeccionAdmin(admin.ModelAdmin):
    list_display = ('id_leccion', 'titulo', 'id_modulo', 'tipo_contenido', 'orden')
    list_filter = ('tipo_contenido',)

@admin.register(ProgresoLeccion)
class ProgresoLeccionAdmin(admin.ModelAdmin):
    list_display = ('id_progreso', 'id_inscripcion', 'id_leccion', 'completada', 'tiempo_dedicado_min')
    list_filter = ('completada',)

@admin.register(Evaluacion)
class EvaluacionAdmin(admin.ModelAdmin):
    list_display = ('id_evaluacion', 'titulo', 'id_curso', 'id_modulo', 'tipo', 'puntaje_maximo', 'fecha_limite')
    list_filter = ('tipo',)

@admin.register(Pregunta)
class PreguntaAdmin(admin.ModelAdmin):
    list_display = ('id_pregunta', 'id_evaluacion', 'tipo', 'puntaje')

@admin.register(OpcionRespuesta)
class OpcionRespuestaAdmin(admin.ModelAdmin):
    list_display = ('id_opcion', 'id_pregunta', 'texto', 'es_correcta')
    list_filter = ('es_correcta',)

@admin.register(IntentoEvaluacion)
class IntentoEvaluacionAdmin(admin.ModelAdmin):
    list_display = ('id_intento', 'id_evaluacion', 'id_inscripcion', 'puntaje_obtenido', 'aprobado', 'fecha_intento')
    list_filter = ('aprobado',)

@admin.register(RespuestaEstudiante)
class RespuestaEstudianteAdmin(admin.ModelAdmin):
    list_display = ('id_respuesta', 'id_intento', 'id_pregunta')

@admin.register(Calificacion)
class CalificacionAdmin(admin.ModelAdmin):
    list_display = ('id_calificacion', 'id_inscripcion', 'promedio', 'aprobado', 'fecha_emision')
    list_filter = ('aprobado',)

@admin.register(Certificado)
class CertificadoAdmin(admin.ModelAdmin):
    list_display = ('id_certificado', 'codigo_unico', 'id_calificacion', 'fecha_emision')
    search_fields = ('codigo_unico',)

@admin.register(ComentarioForo)
class ComentarioForoAdmin(admin.ModelAdmin):
    list_display = ('id_comentario', 'id_curso', 'id_usuario', 'fecha_publicacion', 'activo')
    list_filter = ('activo',)

@admin.register(Pago)
class PagoAdmin(admin.ModelAdmin):
    list_display = ('id_pago', 'id_inscripcion', 'monto', 'moneda', 'metodo', 'estado', 'fecha_pago')
    list_filter = ('estado', 'metodo', 'moneda')