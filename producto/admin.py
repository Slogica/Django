from django.contrib import admin
from .models import Producto

# Registrar el modelo Producto para que pueda ser gestionado a través del panel de administración de Django
admin.site.register(Producto)
