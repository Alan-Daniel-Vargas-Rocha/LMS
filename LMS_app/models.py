from django.db import models

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
   
    password_hash = models.CharField(max_length=255) 
    fecha_registro = models.DateTimeField(auto_now_add=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Rol(models.Model):
    id_rol = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, unique=True)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre

class UsuarioRol(models.Model):
    id_usuario_rol = models.AutoField(primary_key=True)
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    id_rol = models.ForeignKey(Rol, on_delete=models.CASCADE)
    fecha_asignacion = models.DateTimeField(auto_now_add=True)

class Categoria(models.Model):
    id_categoria = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True, null=True)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre

class Curso(models.Model):
    id_curso = models.AutoField(primary_key=True)
    id_categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    id_instructor = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200) # Ajustado a 200 según diagrama
    slug = models.SlugField(max_length=220, unique=True) # Ajustado a 220
    descripcion = models.TextField(blank=True, null=True)
    nivel = models.CharField(max_length=20) # Faltaba
    precio = models.DecimalField(max_digits=10, decimal_places=2) # Faltaba
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True) # Diagrama dice actualizado
    publicado = models.BooleanField(default=True)

    def __str__(self):
        return self.titulo

class Modulo(models.Model):
    id_modulo = models.AutoField(primary_key=True)
    id_curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200) # Ajustado a 200
    orden = models.PositiveIntegerField()
    descripcion = models.TextField(blank=True, null=True)
    creado = models.DateTimeField(auto_now_add=True) # Diagrama dice creado
    actualizado = models.DateTimeField(auto_now=True) # Diagrama dice actualizado
    
    def __str__(self):
        return self.titulo

class Inscripcion(models.Model):
    id_inscripcion = models.AutoField(primary_key=True)
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    id_curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    fecha_inscripcion = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=20, choices=[('activo', 'Activo'), ('inactivo', 'Inactivo')], default='activo')
    progreso_porcentaje = models.DecimalField(max_digits=5, decimal_places=2, default=0.00) # Nombre ajustado

    def __str__(self):
        return f"{self.id_usuario} - {self.id_curso}"

class Leccion(models.Model):
    id_leccion = models.AutoField(primary_key=True)
    id_modulo = models.ForeignKey(Modulo, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200) # Ajustado a 200
    tipo_contenido = models.CharField(max_length=20) # Faltaba (video, texto, pdf...)
    url_contenido = models.CharField(max_length=500, blank=True, null=True) # Faltaba
    duracion_minutos = models.IntegerField(blank=True, null=True) # Faltaba
    orden = models.PositiveIntegerField()
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titulo

class ProgresoLeccion(models.Model):
    id_progreso = models.AutoField(primary_key=True)
    id_inscripcion = models.ForeignKey(Inscripcion, on_delete=models.CASCADE)
    id_leccion = models.ForeignKey(Leccion, on_delete=models.CASCADE)
    completada = models.BooleanField(default=False)
    fecha_completado = models.DateTimeField(blank=True, null=True)
    tiempo_dedicado_min = models.IntegerField(default=0)

    def __str__(self):
        return f"Progreso {self.id_progreso}"

class Evaluacion(models.Model):
    id_evaluacion = models.AutoField(primary_key=True)
    id_curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    id_modulo = models.ForeignKey(Modulo, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    tipo = models.CharField(max_length=20, choices=[('examen', 'Examen'), ('tarea', 'Tarea')])
    puntaje_maximo = models.DecimalField(max_digits=5, decimal_places=2)
    fecha_limite = models.DateTimeField()
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.titulo

class Pregunta(models.Model):
    id_pregunta = models.AutoField(primary_key=True)
    id_evaluacion = models.ForeignKey(Evaluacion, on_delete=models.CASCADE)
    enunciado = models.TextField()
    tipo = models.CharField(max_length=20) # multiple, abierta, etc.
    puntaje = models.IntegerField()

    def __str__(self):
        return f"Pregunta {self.id_pregunta}"

class OpcionRespuesta(models.Model):
    id_opcion = models.AutoField(primary_key=True)
    id_pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
    texto = models.CharField(max_length=500)
    es_correcta = models.BooleanField(default=False)

    def __str__(self):
        return self.texto

class IntentoEvaluacion(models.Model):
    id_intento = models.AutoField(primary_key=True)
    id_evaluacion = models.ForeignKey(Evaluacion, on_delete=models.CASCADE)
    id_inscripcion = models.ForeignKey(Inscripcion, on_delete=models.CASCADE)
    fecha_intento = models.DateTimeField(auto_now_add=True)
    puntaje_obtenido = models.DecimalField(max_digits=6, decimal_places=2)
    aprobado = models.BooleanField(default=False)

    def __str__(self):
        return f"Intento {self.id_intento}"

class RespuestaEstudiante(models.Model):
    id_respuesta = models.AutoField(primary_key=True)
    id_intento = models.ForeignKey(IntentoEvaluacion, on_delete=models.CASCADE)
    id_pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
    id_opcion = models.ForeignKey(OpcionRespuesta, on_delete=models.CASCADE, null=True, blank=True)
    texto_abierto = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Respuesta {self.id_respuesta}"

class Calificacion(models.Model):
    id_calificacion = models.AutoField(primary_key=True)
    id_inscripcion = models.ForeignKey(Inscripcion, on_delete=models.CASCADE)
    promedio = models.DecimalField(max_digits=5, decimal_places=2)
    fecha_emision = models.DateTimeField(auto_now_add=True)
    aprobado = models.BooleanField(default=False)

    def __str__(self):
        return f"Calificacion {self.id_calificacion}"

class Certificado(models.Model):
    id_certificado = models.AutoField(primary_key=True)
    id_calificacion = models.ForeignKey(Calificacion, on_delete=models.CASCADE)
    codigo_unico = models.CharField(max_length=100, unique=True)
    fecha_emision = models.DateTimeField(auto_now_add=True)
    url_pdf = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.codigo_unico

class ComentarioForo(models.Model):
    id_comentario = models.AutoField(primary_key=True)
    id_curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    id_comentario_padre = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    contenido = models.TextField()
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return f"Comentario {self.id_comentario}"

class Pago(models.Model):
    id_pago = models.AutoField(primary_key=True)
    id_inscripcion = models.ForeignKey(Inscripcion, on_delete=models.CASCADE)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    moneda = models.CharField(max_length=3) # Ej: USD, EUR
    metodo = models.CharField(max_length=30) # Ej: tarjeta, paypal
    estado = models.CharField(max_length=20) # Ej: pendiente, completado
    transaccion_externa = models.CharField(max_length=200, blank=True, null=True)
    ultimos_4_digitos = models.CharField(max_length=4, blank=True, null=True)
    fecha_pago = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Pago {self.id_pago}"
    
