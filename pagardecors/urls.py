from django.urls import path
from . import views

urlpatterns = [
    path('', views.ardecors, name="ardecors"),
    path('Iniciarsesion/', views.Iniciarsesion, name="Iniciarsesion"),
    path('contacto/', views.contacto, name="contacto"),
    path('productos/', views.productos, name="productos"),
    path('sobre/', views.sobre, name="sobre"),
      
]