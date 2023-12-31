from django.db import models
from applications.autor.models import Autor
# Create your models here.


class Categoria(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre
    

class Libro(models.Model):
    categoria = models.ForeignKey(
        Categoria,on_delete=models.CASCADE
        )
    autores = models.ManyToManyField(Autor)
    titulo = models.CharField(max_length=50)
    fecha = models.DateTimeField('fecha de lanzamiento')
    portada = models.ImageField( upload_to='portada' )  
    visitas = models.PositiveIntegerField()

    def __str__(self):
        return self.titulo

