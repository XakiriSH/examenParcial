from django.urls import path
from . import views

urlpatterns = [
    path('tiendas/', views.tiendas, name='tiendas'),
    path('productos/', views.productos, name='productos'),
    path('detalle_tienda/<int:tienda_id>/', views.detalle_tienda, name='detalle_tienda'),
    
]
