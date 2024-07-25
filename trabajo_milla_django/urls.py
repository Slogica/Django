import django
"""
URL configuration for trabajo_milla_django project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.contrib import admin
from django.urls import include, path
from producto import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('contacto/', views.contacto, name='contacto'),
    path('envios/', views.envios, name='envios'),
    path('nosotros/', views.nosotros, name='nosotros'),
    path('productos/tienda/', views.tienda, name='tienda'),
    path('productos/list/', views.listar_productos, name='listar_productos'),
    path('productos/crear/', views.agregar_producto, name='agregar_producto'),
    path('productos/editar/', views.editarProductos, name='editarProductos'),
    path('carrito/', views.carrito, name='carrito'),
    path('admini/', views.admini, name='admini'),
    path('productos/', include('producto.urls')),
]
