from django.shortcuts import render, redirect

# Create your views here.

def ardecors(request):
    return render(request, 'ardecors.html')

def Iniciarsesion(request):
    return render(request, 'Iniciarsesion.html')

def contacto(request):
    return render(request, 'contacto.html')

def productos(request):
    return render(request, 'productos.html')

def sobre(request):
    return render(request, 'sobre.html')

def msobre(request):
    return redirect('sobre')
