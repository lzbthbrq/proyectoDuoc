from django.urls import path, re_path
from .views import index, Registro_pago_cm,Registro_producto,Registro_Orden_Pedido,Orden_Compra,oc_producto,Eliminar_Producto,modificar,Registro_proveedor,Eliminar_proveedor,Modificar_proveedor,Lista_proveedores
from . import views
 
urlpatterns = [ 
    path('',index,name='index'),
    path('Registropago',Registro_pago_cm,name='Registro_pago_cm'),
    path('Registro_producto',Registro_producto,name='Registro_producto'),
    path('OrdenPedido',Registro_Orden_Pedido,name='Registro_Orden_Pedido'),
    path('OrdenCompra',Orden_Compra,name='Orden_Compra'),
    path('Filtrar/<razon_social>',oc_producto,name='oc_producto'),
    path('Eliminar_Producto/<codigo_producto>', Eliminar_Producto, name='Eliminar_Producto'),
    path('modificar/<id>', modificar, name='modificar'),
    path('Registro_producto',Registro_producto,name='Registro_producto'),
    path('Registro_proveedor',Registro_proveedor,name='Registro_proveedor'),
    path('Eliminar_proveedor/<razon_social>/', Eliminar_proveedor, name='Eliminar_proveedor'),
    path('Modificar_proveedor/<razon_social>/', Modificar_proveedor, name='Modificar_proveedor'),
    path('Lista_proveedores', Lista_proveedores, name='Lista_proveedores')
] 
