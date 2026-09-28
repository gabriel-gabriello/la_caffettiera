
# Importaciones

from django.urls import path

from core.views import get_home, get_about, get_servicios, get_contacto, get_blog, prueba

# Ambito global

urlpatterns = [

    path("home/", get_home, name="home"),

    path("about/", get_about, name="about"),

    path("servicios/", get_servicios, name="servicios"),

    path("contacto/", get_contacto, name="contacto"),

    path("blog/", get_blog, name="blog"),

    path("prueba/", prueba)

]
