
# Importaciones

from django.db import models

# Models

class Servicio (models.Model):

    # Atributos de clase

    titulo = models.CharField(max_length=200, verbose_name="Titulo")
    subtitulo = models.CharField(max_length=200, verbose_name="Subtitulo")
    descripcion = models.TextField(verbose_name="Descripcion")
    imagen = models.ImageField(upload_to="servicios/", verbose_name="Titulo")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # Clases internas

    class Meta:

        # Atributos de clase

        verbose_name = "Servicio"
        verbose_name_plural = "Servicios"
        db_table = "servicios"

    # Metodos especiales

    def __str__(self):
        return self.titulo