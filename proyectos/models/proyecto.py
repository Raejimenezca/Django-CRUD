from django.db import models

class Proyecto(models.Model):
    nombre = models.CharField(max_length=100, primary_key=True)
    descripcion = models.TextField()
    fecha_inicio = models.DateField()

    def __str__(self):
        return self.nombre