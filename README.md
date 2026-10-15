# LMS
# LMS IDESMA — Backend API

API REST para la plataforma de gestión de aprendizaje **LMS IDESMA**, desarrollada con Django y Django REST Framework. Permite gestionar usuarios, roles, cursos, módulos, lecciones, inscripciones, evaluaciones, certificados y pagos.

---

## 🛠️ Stack Tecnológico

| Categoría | Tecnología |
|---|---|
| Lenguaje | Python 3.14 |
| Framework | Django 6.1.2 |
| API | Django REST Framework |
| Autenticación | JWT (SimpleJWT) |
| Base de datos | PostgreSQL |
| Contenedores | Docker + Docker Compose |
| Documentación | drf-spectacular (Swagger/OpenAPI) |
| CORS | django-cors-headers |

---

## 📋 Requisitos previos

- Python 3.11 o superior
- Docker y Docker Compose instalados
- PostgreSQL (vía Docker o local)
- Git

---

## 🚀 Instalación y configuración

### 1. Clonar el repositorio

```bash
git clone <url-del-repo>
cd Prueba
2. Crear y activar entorno virtual
bash
python -m venv Entorno
# Windows
Entorno\Scripts\activate
# Linux/Mac
source Entorno/bin/activate
3. Instalar dependencias
bash
pip install -r requirements.txt
4. Configurar variables de entorno
Crea un archivo .env en la raíz con:

env
SECRET_KEY=tu_secret_key_aqui
DEBUG=True
DB_NAME=LMS_IDESMA
DB_USER=Alantonic_Gamer
DB_PASSWORD=abc123
DB_HOST=127.0.0.1
DB_PORT=5433
5. Levantar PostgreSQL con Docker
bash
docker compose up -d
6. Aplicar migraciones
bash
python manage.py migrate
7. (Opcional) Cargar datos de prueba
bash
python manage.py seed_data
8. Crear superusuario
bash
python manage.py createsuperuser
9. Levantar el servidor
bash
python manage.py runserver
La API estará disponible en: http://127.0.0.1:8000/api/

📁 Estructura del proyecto
text
Prueba/
├── LMS_app/
│   ├── migrations/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py           # 18 modelos del LMS
│   ├── serializers.py      # Serializers de DRF
│   ├── urls.py             # Rutas de la app
│   └── views.py            # ViewSets y vistas
├── LMS_IDESMA/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
├── docker-compose.yml
├── requirements.txt
└── README.md
🗄️ Modelo de datos
El sistema cuenta con 18 entidades organizadas en 5 dominios:

Autenticación y usuarios
Usuario

Rol

UsuarioRol

Cursos y contenido
Categoria

Curso

Modulo

Leccion

Inscripciones y progreso
Inscripcion

ProgresoLeccion

Evaluaciones
Evaluacion

Pregunta

OpcionRespuesta

IntentoEvaluacion

RespuestaEstudiante

Calificacion

Certificado

Interacción y pagos
ComentarioForo

Pago

🔌 Endpoints principales
Base URL: http://127.0.0.1:8000/api/

Autenticación
Método	Endpoint	Descripción
POST	/auth/registro/	Registro de nuevo usuario
POST	/auth/login/	Inicio de sesión (devuelve JWT)
POST	/auth/refresh/	Renovar token de acceso
Recursos (CRUD vía ViewSets)
Recurso	Endpoint
Usuarios	/usuarios/
Roles	/roles/
Categorías	/categorias/
Cursos	/cursos/
Módulos	/modulos/
Lecciones	/lecciones/
Inscripciones	/inscripciones/
Progreso	/progreso/
Evaluaciones	/evaluaciones/
Preguntas	/preguntas/
Opciones de respuesta	/opciones/
Intentos	/intentos/
Calificaciones	/calificaciones/
Certificados	/certificados/
Foro	/foro/
Pagos	/pagos/
Acciones especiales
Método	Endpoint	Descripción
POST	/cursos/{id}/inscribirse/	Inscribirse a un curso
GET	/docs/	Documentación Swagger
GET	/schema/	Esquema OpenAPI
🔐 Autenticación con JWT
1. Registro
http
POST /api/auth/registro/
Content-Type: application/json

{
  "nombre": "Juan",
  "apellido": "Pérez",
  "email": "juan@example.com",
  "password": "abc12345"
}
2. Login
http
POST /api/auth/login/
Content-Type: application/json

{
  "email": "juan@example.com",
  "password": "abc12345"
}
Respuesta:

json
{
  "access": "eyJhbGciOiJIUzI1NiIs...",
  "refresh": "eyJhbGciOiJIUzI1NiIs..."
}
3. Usar el token
En cada petición protegida:

http
Authorization: Bearer <access_token>
🐳 Docker
Levantar servicios
bash
docker compose up -d
Ver logs
bash
docker compose logs -f
Detener servicios
bash
docker compose down
Reconstruir imágenes
bash
docker compose up -d --build
🧪 Pruebas con Postman
Importa la colección (si está disponible).

Configura la variable base_url = http://127.0.0.1:8000/api/.

Registra un usuario en /auth/registro/.

Haz login en /auth/login/ y copia el access token.

Configura el header Authorization: Bearer <token> a nivel de colección.

Prueba los endpoints CRUD.

🧩 Comandos útiles
bash
# Crear migraciones
python manage.py makemigrations

# Aplicar migraciones
python manage.py migrate

# Cargar datos de prueba
python manage.py seed_data

# Crear superusuario
python manage.py createsuperuser

# Abrir shell interactivo
python manage.py shell

# Recolectar archivos estáticos
python manage.py collectstatic
📚 Documentación de la API
Una vez levantado el servidor:

Swagger UI: http://127.0.0.1:8000/api/docs/

Esquema OpenAPI: http://127.0.0.1:8000/api/schema/

Admin de Django: http://127.0.0.1:8000/admin/

🔒 Seguridad
Contraseñas hasheadas con make_password (bcrypt/PBKDF2).

Autenticación mediante JWT.

CORS configurado para el frontend.

Validación de datos en serializers.

Variables sensibles en .env (no versionadas).

🧭 Roadmap
☑ Modelo de datos (18 entidades)
☑ Migraciones aplicadas
☑ API REST funcional
☑ Autenticación JWT
☑ Documentación Swagger
□ Permisos por rol
□ Endpoints especiales (progreso, quiz, certificado)
□ Frontend (React + Tailwind)
□ Despliegue en producción
👥 Autores
Alan — Desarrollo backend

Requirements limpio:
asgiref==3.12.1
attrs==26.1.0
Django==6.1.2
django-cors-headers==4.9.0
djangorestframework==3.18.3
djangorestframework_simplejwt==5.5.1
drf-spectacular==0.30.0
inflection==0.5.1
jsonschema==4.26.0
jsonschema-specifications==2025.9.1
psycopg==3.3.6
psycopg-binary==3.3.6
PyJWT==2.15.1
PyYAML==6.0.3
referencing==0.37.0
rpds-py==2026.9.1
sqlparse==0.6.0
tzdata==2026.5
uritemplate==4.2.0

Proyecto académico — LMS IDESMA

