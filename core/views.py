
# Importaciones

from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, FileResponse, Http404
from django.conf import settings

from servicios.models import Servicio

from pathlib import Path

import os

# Views

def get_home(http_request:HttpRequest):

    return render(http_request, "core/home.html")

def get_about(http_request:HttpRequest):

    return render(http_request, "core/about.html")

def get_servicios(http_request:HttpRequest):

    return render(http_request, "core/servicios.html")

def get_contacto(http_request:HttpRequest):

    return render(http_request, "core/contacto.html")

def get_blog(http_request:HttpRequest):

    return render(http_request, "core/blog.html")

def prueba(http_request:HttpRequest):

    servicio = Servicio.objects.get(id=4)

    ruta = servicio.imagen.path

    return HttpResponse(
        f"""
        Nombre: {servicio.imagen.name}<br>
        Ruta: {ruta}<br>
        Existe: {os.path.exists(ruta)}<br>
        Tamaño: {os.path.getsize(ruta) if os.path.exists(ruta) else 'NO EXISTE'}
        """
    )

# Es la funcion servidora de archivos media

def servir_media(request:HttpRequest, path):

    archivo = Path(settings.MEDIA_ROOT) / path

    if not archivo.is_file():
        raise Http404("Archivo no encontrado")

    archivo_abierto = open(archivo, "rb")

    return FileResponse(archivo_abierto)

