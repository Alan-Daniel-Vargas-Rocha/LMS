from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from .models import (
    Usuario, Rol, Categoria, Curso, Modulo, Leccion,
    Inscripcion, ProgresoLeccion, Evaluacion, Pregunta,
    OpcionRespuesta, IntentoEvaluacion, RespuestaEstudiante,
    Calificacion, Certificado, ComentarioForo, Pago
)
from .serializers import *


class RegistroView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = UsuarioRegistroSerializer(data=request.data)
        if serializer.is_valid():
            usuario = serializer.save()
            refresh = RefreshToken.for_user(usuario)
            return Response({
                'usuario': UsuarioSerializer(usuario).data,
                'access': str(refresh.access_token),
                'refresh': str(refresh),
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer


class RolViewSet(viewsets.ModelViewSet):
    queryset = Rol.objects.all()
    serializer_class = RolSerializer


class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer


class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.filter(publicado=True)
    serializer_class = CursoSerializer

    @action(detail=True, methods=['post'], permission_classes=[permissions.IsAuthenticated])
    def inscribirse(self, request, pk=None):
        curso = self.get_object()
        inscripcion, creada = Inscripcion.objects.get_or_create(
            id_usuario=request.user,
            id_curso=curso,
        )
        if not creada:
            return Response({'detail': 'Ya estás inscrito.'}, status=400)
        return Response(InscripcionSerializer(inscripcion).data, status=201)


class ModuloViewSet(viewsets.ModelViewSet):
    queryset = Modulo.objects.all()
    serializer_class = ModuloSerializer


class LeccionViewSet(viewsets.ModelViewSet):
    queryset = Leccion.objects.all()
    serializer_class = LeccionSerializer


class InscripcionViewSet(viewsets.ModelViewSet):
    serializer_class = InscripcionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Inscripcion.objects.filter(id_usuario=self.request.user)


class ProgresoLeccionViewSet(viewsets.ModelViewSet):
    queryset = ProgresoLeccion.objects.all()
    serializer_class = ProgresoLeccionSerializer


class EvaluacionViewSet(viewsets.ModelViewSet):
    queryset = Evaluacion.objects.all()
    serializer_class = EvaluacionSerializer


class PreguntaViewSet(viewsets.ModelViewSet):
    queryset = Pregunta.objects.all()
    serializer_class = PreguntaSerializer


class OpcionRespuestaViewSet(viewsets.ModelViewSet):
    queryset = OpcionRespuesta.objects.all()
    serializer_class = OpcionRespuestaSerializer


class IntentoEvaluacionViewSet(viewsets.ModelViewSet):
    queryset = IntentoEvaluacion.objects.all()
    serializer_class = IntentoEvaluacionSerializer


class CalificacionViewSet(viewsets.ModelViewSet):
    queryset = Calificacion.objects.all()
    serializer_class = CalificacionSerializer


class CertificadoViewSet(viewsets.ModelViewSet):
    queryset = Certificado.objects.all()
    serializer_class = CertificadoSerializer


class ComentarioForoViewSet(viewsets.ModelViewSet):
    queryset = ComentarioForo.objects.filter(activo=True)
    serializer_class = ComentarioForoSerializer


class PagoViewSet(viewsets.ModelViewSet):
    queryset = Pago.objects.all()
    serializer_class = PagoSerializer