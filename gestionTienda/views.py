from django.shortcuts import render

def tiendas(request):
    # Implementa la lógica para mostrar la lista de tiendas
    return render(request, 'tiendas.html')

def productos(request):
    # Implementa la lógica para mostrar la lista de productos
    return render(request, 'productos.html')

def detalle_tienda(request, tienda_id):
    # Implementa la lógica para mostrar los detalles de una tienda
    return render(request, 'detalle_tienda.html')