from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('', views.ardecors, name="ardecors"),
    path('iniciar_sesion/', views.iniciar_sesion, name='iniciar_sesion'),
    path('', views.index, name='index'),
    path('registro/', views.registro, name='registro'),  # Cambié 'registrar' a 'registro'
    path('cerrar_sesion/', views.cerrar_sesion, name='cerrar_sesion'),
    path('contacto/', views.contacto, name="contacto"),
    path('productos/', views.productos, name="productos"),
    path('productos/crear', views.crear, name='crear'),
    path('productos/editar/<int:id>/', views.editar, name='editar'),
    path('productos/eliminar/<int:id>/', views.eliminar, name='eliminar'),
    path('sobre/', views.sobre, name="sobre"),
    path('msobre/', views.msobre, name="msobre"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)