from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Producto
from .forms import ProductoForm

# existen 2 tipos de parametros que se usan en las peticiones http 
# 1- Request
# 2- Response
# Create your views here.

def inicio(request):
    return render(request, 'pages/inicio.html')

def listadoProductos(request):
    productos = Producto.objects.all()
    return render(request,'producto/productos.html', {'productos': productos})

def crearProducto(request):
    formulario = ProductoForm(request.POST or None)

    if formulario.is_valid():
        # producto = formulario.save
        formulario.save()
        return redirect('productos')

    return render(request, 'producto/crear.html', {'formulario':formulario})

def editarProducto(request, id):
    producto = Producto.objects.get(id = id)

    formulario = ProductoForm(request.POST or None, instance= producto)
    
    if formulario.is_valid():
        formulario.save()
        return redirect('productos')
    
    return render(request, 'producto/editar.html', {'formulario':formulario})

def eliminarProducto(request, id):
    producto = Producto.objects.get(id = id)
    producto.delete()
    return redirect('productos')
