from django.urls import path
from . import views

urlpatterns = [
    path('', views.ardecors, name="ardecors"),
    path('Iniciarsesion/', views.Iniciarsesion, name="Iniciarsesion"),
    path('contacto/', views.contacto, name="contacto"),
    path('productos/', views.contacto, name="productos"),
    path('sobre/', views.contacto, name="sobre"),
]