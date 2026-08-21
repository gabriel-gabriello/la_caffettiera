
# Importaciones

from django.contrib import admin

from servicios.models import Servicio

# Clases ModelAdmin

class ServicioAdmin (admin.ModelAdmin):

    # Atributos de clase

    readonly_fields = ("created", "updated")
    list_display = ("id", "titulo", "subtitulo", "imagen", "created", "updated")

# Ambito global

admin.site.register(Servicio, ServicioAdmin)