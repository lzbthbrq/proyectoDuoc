from django.contrib import admin

from .models import Empleados,Rol_Empleados,Cliente_Moroso,Proveedor,Producto,StockProductos,Pedidos,Venta,Boleta

admin.site.register(Empleados)
admin.site.register(Rol_Empleados)
admin.site.register(Cliente_Moroso)
admin.site.register(Proveedor)
admin.site.register(Producto)
admin.site.register(StockProductos)
admin.site.register(Pedidos)
admin.site.register(Venta)
admin.site.register(Boleta)