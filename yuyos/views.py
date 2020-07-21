from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views import generic
from .models import Cliente_Moroso,Boleta,Ficha_Cliente_Moroso,Pago_Cliente_Moroso,Producto,Proveedor,Pedidos
from django.contrib import messages

def index(request):
    return render(request,'index.html',)

def Registro_pago_cm(request):
    return render(request,'Registro_pago_cm.html',)

def listarproveedor(request):
    prov = Proveedor.objects.all()

    try:
        mensaje = "Se ha guardado el producto correctamente"
        messages.success(request, mensaje)
    except:
        mensaje = "Se ha guardado el producto correctamente"
        messages.error(request, mensaje)

    return render(request,'Registro_producto.html',{'prov':prov})
 
def Registro_producto(request):
    prov = Proveedor.objects.all()
    produ = Producto.objects.all()
    variables = {
        'prov':prov,
        'produ':produ
    }

    if request.POST:
        Produ = Producto()
        Produ.codigo_producto = request.POST.get('codproducto')
        Produ.nombre_producto = request.POST.get('nomprodu')
        Produ.fecha_vencimiento = request.POST.get('fechavencimiento')
        Produ.tipo_producto = request.POST.get('tipoproducto')
        Produ.razon_social_proveedor = Proveedor.objects.get(razon_social =request.POST.get('razonsocialprov'))
        Produ.fecha_vencimiento = request.POST.get('fechavencimiento')
        Produ.precio_unitario = request.POST.get('punitario')
          
    try:
        Produ.save()
        variables['mensaje']= 'El producto se ha registrado correctamente'
    except:
        variables['mensaje']= 'El producto no se guardó'

    return render(request, 'Registro_producto.html',variables)

def Registro_Orden_Pedido(request):
    return render(request, 'Registro_Orden_Pedido.html')

def Orden_Compra(request):
    prov = Proveedor.objects.all()
    variables = {
        'prov':prov,
    }
    return render(request, 'Orden_Compra.html',variables)

def oc_producto(request,razon_social):
    prod = Producto.objects.get(razon_social_proveedor=razon_social)
    variables = {
        'prod':prod
    }
    return redirect(request, 'Orden_Compra.html',variables)
    
def Eliminar_Producto(request,codigo_producto,*args , **kwargs):
    produ = Producto.objects.get(codigo_producto=codigo_producto)
    produ.delete(*args , **kwargs)
    input('delete')
    try:
        
        mensaje = "Se ha eliminado correctamente"
        messages.success(request, mensaje)
    except:
        mensaje = "No se ha podido eliminar"
        messages.error(request, mensaje)

    return redirect('Registro_producto')
  
def modificar(request,id):    
    return render(request, 'Registro_producto.html')
    return render(request, 'Registro_producto.html',variables)

def Registro_proveedor(request):

    if request.POST:
        Prove = Proveedor()
        Prove.razon_social = request.POST.get('razon_social')
        Prove.nombre_prov = request.POST.get('nombre_prov')
        Prove.Nombre_Representante = request.POST.get('Nombre_Representante')
        Prove.Representante_Apellido = request.POST.get('Representante_Apellido')
        Prove.direccion = request.POST.get('direccion')
        Prove.telefono = request.POST.get('telefono')
        Prove.correo = request.POST.get('correo')
        Prove.rubro = request.POST.get('rubro')

        try:
            Prove.save()
            mensaje = "Se ha guardado el producto correctamente"
            messages.success(request, mensaje)
        except:
            mensaje = "Se ha guardado el producto correctamente"
            messages.error(request, mensaje)
    return render(request, 'Registro_proveedor.html')

def Eliminar_proveedor(request,razon_social,*args, **kwargs):
        prove = Proveedor.objects.get(razon_social=razon_social)

        try:
            prove.delete(*args, **kwargs)
            mensaje = "Eliminado Correctamente"
            messages.success(request, mensaje)
        except:
            mensaje = "No se ha podido eliminar"
            messages.error(request, mensaje)
        return render('Lista_proveedores')

def Modificar_proveedor(request,razon_social):
    Prove = Proveedor.objects.get(razon_social=razon_social)
    
    if request.POST:
        Prove=razon_social()
        Prove.razon_social = request.POST.get('razon_social')
        Prove.nombre_prov = request.POST.get('nombre_prov')
        Prove.Nombre_Representante = request.POST.get('Nombre_Representante')
        Prove.Representante_Apellido = request.POST.get('Representante_Apellido')
        Prove.direccion = request.POST.get('direccion')
        Prove.telefono = request.POST.get('telefono')
        Prove.correo = request.POST.get('correo')
        Prove.rubro = request.POST.get('rubro')

        try: 
            Prove.save()
            mensaje = 'Proveedor Guardado Correctamente'
            messages.success(request, mensaje)
        except:
            mensaje = 'No se pudo Guardar'
            messages.error(request, mensaje)


def Lista_proveedores(request):
    Prove = Proveedor.objects.all()

    return render(request, 'Lista_proveedores.html', {
        'Prove': Prove
    })
