from django.shortcuts import render, redirect, get_object_or_404
from .models import Proveedor

# Listar proveedores
def index(request):
    proveedores = Proveedor.objects.all()
    return render(request, 'listar_proveedores.html', {'proveedores': proveedores})

# Agregar proveedor
def agregar_proveedor(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        direccion = request.POST['direccion']
        telefono = request.POST['telefono']
        correo = request.POST['correo']
        tipo_suministro = request.POST['tipo_suministro']
        Proveedor.objects.create(
            nombre=nombre,
            direccion=direccion,
            telefono=telefono,
            correo=correo,
            tipo_suministro=tipo_suministro
        )
        return redirect('inicio')
    return render(request, 'agregar_proveedor.html')

# Editar proveedor
def editar_proveedor(request, id):
    proveedor = get_object_or_404(Proveedor, id=id)
    if request.method == 'POST':
        proveedor.nombre = request.POST['nombre']
        proveedor.direccion = request.POST['direccion']
        proveedor.telefono = request.POST['telefono']
        proveedor.correo = request.POST['correo']
        proveedor.tipo_suministro = request.POST['tipo_suministro']
        proveedor.save()
        return redirect('inicio')
    return render(request, 'editar_proveedor.html', {'proveedor': proveedor})

# Borrar proveedor
def borrar_proveedor(request, id):
    proveedor = get_object_or_404(Proveedor, id=id)
    if request.method == 'POST':
        proveedor.delete()
        return redirect('inicio')
    return render(request, 'borrar_proveedor.html', {'proveedor': proveedor})
