from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Producto
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .models import Producto
#from .forms import ArdecorForm

def ardecors(request):
    return render(request, 'ardecors.html')

def iniciar_sesion(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return render(request, 'iniciar_sesion.html', {'error': 'Usuario o contraseña incorrectos'})
    return render(request, 'iniciar_sesion.html')

def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('iniciar_sesion')
    else:
        form = UserCreationForm()
    return render(request, 'registro.html', {'form': form})

def contacto(request):
    return render(request, 'contacto.html')

def productos(request):
    productos = Producto.objects.all()
    return render(request, 'productos.html', {'productos': productos})

def crear(request):
    #formulario = ArdecorForm(request.POST or None)
    if request.method == 'POST':
        nombre = request.POST['nombre']
        descripcion = request.POST['descripcion']
        precio = request.POST['precio']
        Producto.objects.create(nombre=nombre, descripcion=descripcion, precio=precio)
        return redirect('index')
    return render(request, 'crear.html')

def editar(request, id):
    producto = get_object_or_404(Producto, id=id)
    if request.method == 'POST':
        producto.nombre = request.POST['nombre']
        producto.descripcion = request.POST['descripcion']
        producto.precio = request.POST['precio']
        producto.save()
        return redirect('index')
    return render(request, 'editar.html', {'producto': producto})

def index(request):
    productos = Producto.objects.all()
    return render(request, 'index.html', {'productos': productos})

def eliminar(request, id):
    producto = get_object_or_404(Producto, id=id)
    if request.method == 'POST':
        producto.delete()
        return redirect('index')
    return redirect('index')

def sobre(request):
    return render(request, 'sobre.html')

def msobre(request):
    return redirect('sobre')

def cerrar_sesion(request):
    logout(request)
    return redirect('iniciar_sesion')