from django.urls import path
from . import views

urlpatterns = [
    # Ruta para la página de inicio
    path('index/', views.index, name='index'),
    
    # Ruta para la página de listado de productos
    path('productos/', views.productos, name='productos'),
    
    # Ruta para listar todos los productos
    path('productos/list/', views.listar_productos, name='listar_productos'),
    
    # Ruta para agregar un nuevo producto (se podría considerar unificar con la ruta de 'crear')
    path('productos/crear/', views.addProductos, name='addProductos'),
    
    # Ruta para editar un producto específico, con ID en la URL
    path('productos/edit/<int:id>/', views.editarProducto, name='editar_producto'),
    
    # Ruta para eliminar un producto específico, con ID en la URL
    path('productos/delete/<int:id>/', views.eliminarProducto, name='eliminar_producto'),
    
    # Ruta para el formulario de agregar producto (este podría ser redundante si ya tienes la ruta de 'crear')
    path('agregar_producto/', views.agregar_producto, name='agregar_producto'),
]