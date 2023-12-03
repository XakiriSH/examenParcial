from django.shortcuts import render
from .models import Tienda, Producto
from .forms import TiendaForm, ProductoForm

def tiendas(request):
    tiendas = Tienda.objects.all()
    if request.method == 'POST':
        # Lógica para agregar una nueva tienda
        form = TiendaForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = TiendaForm()

    return render(request, 'tiendas.html', {'tiendas': tiendas, 'form': form})

def productos(request):
    productos = Producto.objects.all()
    if request.method == 'POST':
        # Lógica para agregar un nuevo producto
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ProductoForm()

    return render(request, 'productos.html', {'productos': productos, 'form': form})

def detalle_tienda(request, tienda_id):
    # Implementa la lógica para mostrar los detalles de una tienda
    return render(request, 'detalle_tienda.html')