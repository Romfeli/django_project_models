from django.db import models
from applications.libro.models import Libro
# Create your models here.


class Lector(models.Model):
    nombre = models.CharField( max_length=50)
    apellidos = models.CharField( max_length=50)
    nacionalidad = models.CharField( max_length=20)
    edad = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.nombre
    

class Prestamo(models.Model):
    lector = models.ForeignKey(Lector, on_delete=models.CASCADE)
    fecha_prestamo = models.DateField()
    fecha_devolucion = models.DateField(blank=True, null=True)
    devuelto = models.BooleanField()


    def __str__(self):
        return self.libro.titulo