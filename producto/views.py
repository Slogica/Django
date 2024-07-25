from django.shortcuts import render, get_object_or_404,redirect
from .forms import ProductoForm
from .models import Producto

# Create your views here.

# Vista para la página de inicio
def index(request):
    return render(request, 'pages/index.html')

# Vista para la página de contacto
def contacto(request):
    return render(request, 'pages/contacto.html')

# Vista para la página de envíos
def envios(request):
    return render(request, 'pages/envios.html')

# Vista para la página de nosotros
def nosotros(request):
    return render(request, 'pages/nosotros.html')

# Vista para la página de la tienda
def tienda(request):
    return render(request, 'pages/productos/tienda.html')

# Vista para la página de productos
def productos(request):
    return render(request, 'pages/productos/list.html')

# Vista para la página de agregar productos
def addProductos(request):
    return render(request, 'pages/productos/crear.html')

# Vista para la página de editar productos
def editarProductos(request):
    return render(request, 'pages/productos/editar.html')

# Vista para la página del carrito
def carrito(request):
    return render(request, 'pages/carrito.html')

# Vista para la página del administrador
def admini(request):
    return render(request, 'pages/admini.html')

# Vista para listar los productos
def listar_productos(request):
    """
    Obtiene todos los productos de la base de datos y los pasa a la plantilla de listado de productos.
    """
    productos = Producto.objects.all()
    return render(request, 'pages/productos/list.html', {'productos': productos})

# Vista para agregar un producto
def agregar_producto(request):
    """
    Maneja el formulario para agregar un nuevo producto. Si el método es POST, valida y guarda el formulario.
    Si el método es GET, muestra un formulario vacío.
    """
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()  # Guardar los datos en la base de datos
            return redirect('listar_productos')  # Redireccionar a la lista de productos
    else:
        form = ProductoForm() # Muestra un formulario vacío

    return render(request, 'pages/productos/crear.html', {'form': form})

# Vista para editar un producto
def editarProducto(request, id):
    producto = get_object_or_404(Producto, id=id) # Obtiene el producto con el ID proporcionado
    """
    Maneja el formulario para editar un producto existente. 
    Si el método es POST, valida y guarda el formulario con los datos del producto existente.
    Si el método es GET, muestra el formulario con los datos del producto.
    """
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save() # Guarda los cambios en el producto
            return redirect('listar_productos') # Redirecciona a la lista de productos
    else:
        form = ProductoForm(instance=producto) # Muestra el formulario con los datos del producto

    
    return render(request, 'pages/productos/editar.html', {'form': form, 'producto': producto})

# Vista para eliminar un producto
def eliminarProducto(request, id):
    """
    Maneja la eliminación de un producto. Si el método es POST, elimina el producto y redirecciona a la lista de productos.
    Si el método es GET, muestra una página de confirmación de eliminación.
    """
    producto = get_object_or_404(Producto, id=id)
    
    if request.method == 'POST':
        producto.delete()
        return redirect('listar_productos')
    
    return render(request, 'pages/productos/eliminar_confirmar.html', {'producto': producto})


