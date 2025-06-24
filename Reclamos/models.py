from django.db import models

class Reclamo(models.Model):
    OPCIONES_TIPO = [
        ('reclamo', 'Reclamo'),
        ('felicitacion', 'Felicitación'),
    ]

    rut = models.CharField(max_length=12)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    fecha = models.DateField()
    tipo = models.CharField(max_length=15, choices=OPCIONES_TIPO)
    mensaje = models.TextField()

    def __str__(self):
        return f'{self.tipo.title()} de {self.nombre} {self.apellido}'
