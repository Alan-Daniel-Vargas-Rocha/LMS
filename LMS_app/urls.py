from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

from .views import *

router = DefaultRouter()
router.register('usuarios', UsuarioViewSet)
router.register('roles', RolViewSet)
router.register('categorias', CategoriaViewSet)
router.register('cursos', CursoViewSet)
router.register('modulos', ModuloViewSet)
router.register('lecciones', LeccionViewSet)
router.register('inscripciones', InscripcionViewSet, basename='inscripciones')
router.register('progreso', ProgresoLeccionViewSet)
router.register('evaluaciones', EvaluacionViewSet)
router.register('preguntas', PreguntaViewSet)
router.register('opciones', OpcionRespuestaViewSet)
router.register('intentos', IntentoEvaluacionViewSet)
router.register('calificaciones', CalificacionViewSet)
router.register('certificados', CertificadoViewSet)
router.register('foro', ComentarioForoViewSet)
router.register('pagos', PagoViewSet)

urlpatterns = [
    path('auth/registro/', RegistroView.as_view()),
    path('auth/login/', TokenObtainPairView.as_view()),
    path('auth/refresh/', TokenRefreshView.as_view()),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('docs/', SpectacularSwaggerView.as_view(url_name='schema')),
    path('', include(router.urls)),
]