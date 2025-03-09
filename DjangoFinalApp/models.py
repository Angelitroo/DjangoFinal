from django.db import models


class Tarea(models.Model):
    ESTADOS = [
        ('por_realizar', 'Por realizar'),
        ('en_transito', 'En tránsito'),
        ('completada', 'Completada'),
    ]

    titulo = models.CharField(max_length=255)
    descripcion = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=20, choices=ESTADOS, default='por_realizar')

    def __str__(self):
        return self.titulo
