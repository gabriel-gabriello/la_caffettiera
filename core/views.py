
# Importaciones

from django.shortcuts import render

from django.http import HttpResponse, HttpRequest

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