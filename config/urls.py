
# Importaciones

from django.contrib import admin

from django.urls import path, include

from django.conf import settings

from django.conf.urls.static import static

# Ambito global

urlpatterns = [

    path('admin/', admin.site.urls),

    path("core/", include("core.urls"))

]


# Esta es la buena practica, pero por ahora no pondremos el if ya que no quiero usar un almacenamiendo virtual, pero
# En un futuro lo usare sin duda

"""
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
"""

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
