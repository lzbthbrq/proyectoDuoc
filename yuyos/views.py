from django.shortcuts import render
from django.views import generic
from .models import Cliente_Moroso,Boleta,Ficha_Cliente_Moroso,Pago_Cliente_Moroso,Producto,Proveedor

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