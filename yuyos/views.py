from django.shortcuts import render
from django.views import generic
from .models import Cliente_Moroso,Boleta,Ficha_Cliente_Moroso,Pago_Cliente_Moroso,Producto,Proveedor
from django.contrib import messages

def index(request):
    return render(request,'index.html',)

def Registro_pago_cm(request):
    return render(request,'Registro_pago_cm.html',)

def listarproveedor(request):
    prov = Proveedor.objects.all()
    return render(request,'Registro_producto.html',{'prov':prov})
 
def Registro_producto(request):
    prov = Proveedor.objects.all()
    variables = {
        'prov':prov
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
        Produ.save()
    
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