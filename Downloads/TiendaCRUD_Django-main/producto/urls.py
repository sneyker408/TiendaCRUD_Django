from django.urls import path
from producto import views

urlpatterns = [
    path('', views.inicio, name="inicio"),
    path('producto/', views.listadoProductos, name="productos"),
    path('productos/crear', views.crearProducto, name="crear_producto"),
    path('productos/editar/<int:id>', views.editarProducto, name="editar_producto"),
    path('productos/eliminar/<int:id>', views.eliminarProducto, name="eliminar_producto")
]