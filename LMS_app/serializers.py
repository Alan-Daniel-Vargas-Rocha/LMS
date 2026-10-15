from rest_framework import serializers
from .models import (
    Usuario, Rol, UsuarioRol, Categoria, Curso, Modulo, Leccion,
    Inscripcion, ProgresoLeccion, Evaluacion, Pregunta, OpcionRespuesta,
    IntentoEvaluacion, RespuestaEstudiante, Calificacion, Certificado,
    ComentarioForo, Pago
)


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id_usuario', 'nombre', 'apellido', 'email', 'fecha_registro', 'activo']
        read_only_fields = ['id_usuario', 'fecha_registro']


class UsuarioRegistroSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)

    class Meta:
        model = Usuario
        fields = ['id_usuario', 'nombre', 'apellido', 'email', 'password']

    def create(self, validated_data):
        from django.contrib.auth.hashers import make_password
        validated_data['password_hash'] = make_password(validated_data.pop('password'))
        return super().create(validated_data)


class RolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rol
        fields = '__all__'


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'


class CursoSerializer(serializers.ModelSerializer):
    instructor_nombre = serializers.CharField(source='id_instructor.__str__', read_only=True)
    categoria_nombre = serializers.CharField(source='id_categoria.nombre', read_only=True)

    class Meta:
        model = Curso
        fields = '__all__'
        read_only_fields = ['slug', 'fecha_creacion', 'actualizado']


class ModuloSerializer(serializers.ModelSerializer):
    class Meta:
        model = Modulo
        fields = '__all__'


class LeccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leccion
        fields = '__all__'


class InscripcionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inscripcion
        fields = '__all__'
        read_only_fields = ['fecha_inscripcion', 'progreso_porcentaje']


class ProgresoLeccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProgresoLeccion
        fields = '__all__'


class EvaluacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evaluacion
        fields = '__all__'


class PreguntaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pregunta
        fields = '__all__'


class OpcionRespuestaSerializer(serializers.ModelSerializer):
    class Meta:
        model = OpcionRespuesta
        fields = '__all__'


class IntentoEvaluacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = IntentoEvaluacion
        fields = '__all__'


class RespuestaEstudianteSerializer(serializers.ModelSerializer):
    class Meta:
        model = RespuestaEstudiante
        fields = '__all__'


class CalificacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Calificacion
        fields = '__all__'


class CertificadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificado
        fields = '__all__'


class ComentarioForoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComentarioForo
        fields = '__all__'


class PagoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pago
        fields = '__all__'