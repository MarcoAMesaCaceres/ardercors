from django.urls import include,path
from . import views
from django.conf import settings


urlpatterns = [
    path('', views.ardecors, name="ardecors"),  # URL para la vista index
    path('', views.admin_dashboard, name='admin_dashboard'),
    path('iniciar_sesion/', views.iniciar_sesion, name='iniciar_sesion'),
    path('registro/', views.registro, name='registro'),  # Cambié 'registrar' a 'registro'
    path('cerrar_sesion/', views.cerrar_sesion, name='cerrar_sesion'),

    path('contacto/', views.contacto, name="contacto"),

    path('productos/', views.productos, name="productos"),
    path('productos/crear', views.crear, name='crear'),
    path('productos/editar/<int:id>/', views.editar, name='editar'),
    path('productos/eliminar/<int:id>/', views.eliminar, name='eliminar'),

    path('sobre/', views.sobre, name="sobre"),
    path('msobre/', views.msobre, name="msobre"),

    path('accounts/logout/', views.custom_logout, name='logout'),

    path('usuarios/', views.usuario_list, name='usuario_list'),
    path('usuarios/<int:pk>/', views.usuario_detail, name='usuario_detail'),
    path('usuarios/new/', views.usuario_create, name='usuario_create'),
    path('usuarios/<int:pk>/edit/', views.usuario_update, name='usuario_update'),
    path('usuarios/<int:pk>/delete/', views.usuario_delete, name='usuario_delete'),
    
] 