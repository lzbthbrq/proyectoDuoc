from django.db import models

class Rol_Empleados(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=20)

    def __str__(self):
        return str(self.nombre)

class Empleados(models.Model):
    rut_empleado = models.CharField(primary_key=True, max_length=10)
    primer_nombre = models.CharField(max_length=30)
    segundo_nombre = models.CharField(max_length=30)
    ap_paterno = models.CharField(max_length=30)
    ap_materno = models.CharField(max_length=30)
    rol = models.ForeignKey('Rol_Empleados', on_delete=models.SET_NULL, null=True)
    telefono = models.IntegerField(blank=True, null=True)
    direccion = models.CharField(max_length=50)
    email = models.CharField(max_length=30)

    def __str__(self):
        return str(self.primer_nombre)

class Cliente_Moroso(models.Model):
    rut_cliente_moroso = models.IntegerField(primary_key=True, null=False)
    primer_nombre = models.CharField(max_length=30,null=False)
    segundo_nombre = models.CharField(max_length=30,null=True)
    apellido_paterno = models.CharField(max_length=30,null=False)
    apellido_materno = models.CharField(max_length=30,null=True)
    telefono = models.IntegerField(blank=True, null=True)
    direccion = models.CharField(max_length=50,null=False)
    email = models.CharField(max_length=30, null=False)
    autorizacion_fiado = models.BooleanField(default=False)
    num_ficha = models.ForeignKey('Ficha_Cliente_Moroso', on_delete=models.CASCADE ,null=False)

    def __str__(self):
        return str(self.primer_nombre, self.apellido_paterno)

class Proveedor(models.Model):
    razon_social = models.IntegerField(primary_key=True, unique=True, null=False)
    nombre_prov = models.CharField(max_length=50, null=False)
    Nombre_Representante = models.CharField(max_length=50, null=False)
    Representante_Apellido = models.CharField(max_length=50, null=False)
    direccion = models.CharField(max_length=50, null=False)
    telefono = models.IntegerField(null=False)
    correo = models.CharField(max_length=50, null=False)
    rubro = models.CharField(max_length=50, null=False)

    def __str__(self):
        return f'{self.nombre_prov}, ({self.razon_social})'

class Producto(models.Model):
    codigo_producto = models.IntegerField(primary_key=True, unique=True, null=False)
    nombre_producto = models.CharField(max_length=90, null=False)
    fecha_vencimiento = models.DateField()
    tipo_producto = models.CharField(max_length=50, null=False)
    precio_unitario = models.IntegerField(null=False, default=0)
    razon_social_proveedor = models.ForeignKey('Proveedor', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return str(self.nombre_producto)

class StockProductos(models.Model):
    codigo_producto = models.ForeignKey('Producto', on_delete=models.SET_NULL, null=True)
    nombre_producto = models.CharField(max_length=90, null=False)
    stock_producto = models.IntegerField(default=0, null=False)

    def __str__(self):
        return str(self.stock_producto)

class Pedidos(models.Model):
    nombre_Proveedor = models.CharField(max_length=50, null=False)
    razon_social_proveedor = models.ForeignKey('Proveedor', on_delete=models.SET_NULL, null=True)
    codigo_producto = models.ForeignKey('Producto', on_delete=models.SET_NULL, null=True)
    nombre_producto = models.CharField(max_length=40, null=False)
    cantidad_pedida = models.IntegerField(default=0, null=False)
    precio_unitario = models.IntegerField(default=0, null=False)
    monto_total = models.IntegerField(default=0, null=False)
    numero_orden = models.ForeignKey('Orden_Despacho', on_delete=models.SET_NULL, null=True)
    numero_pedido = models.IntegerField(primary_key=True)
    def __str__(self):
        return str(self.numero_orden, self.nombre_producto)

class Orden_Despacho(models.Model):
    codigo = models.CharField(primary_key=True, max_length=15, null=False, unique=True)
    fecha = models.DateField()
    responzable = models.ForeignKey('Empleados', on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return str(self.codigo, self.fecha, self.responzable)

class Venta(models.Model):
    n_venta = models.IntegerField(primary_key=True, null=False, unique=True)
    fecha = models.DateField()
    codigo_producto = models.ForeignKey('Producto', on_delete=models.SET_NULL, null=True)
    nom_producto = models.CharField(max_length=50, null=False)
    cant_producto = models.IntegerField(default=0, null=False)
    valor_unitario = models.IntegerField(default=0, null=False)
    monto_total = models.IntegerField(default=0, null=False)
    codigo_boleta = models.ForeignKey('Boleta', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return str(self.n_venta, self.monto_total)

class Boleta(models.Model):
    codigo_boleta = models.IntegerField(primary_key=True, null=False, unique=True)
    fecha_emision = models.DateField()
    n_venta = models.ForeignKey('Venta', on_delete=models.SET_NULL, null=True)
    nombre_producto = models.CharField(max_length=30, null=False)
    cod_producto = models.ForeignKey('Producto', on_delete=models.SET_NULL, null=True)
    cant_producto = models.IntegerField(default=0, null=False)
    monto_unitario = models.IntegerField(default=0, null=False)
    monto_total = models.IntegerField(default=0, null=False)
    forma_pago = models.CharField(max_length=25, null=False)

    def __str__(self):
        return str(self.codigo_boleta, self.monto_total)

class Ficha_Cliente_Moroso(models.Model):
    numero_ficha = models.IntegerField(primary_key=True, null=False, unique=True)
    rut_cliente_moroso = models.ForeignKey('Cliente_Moroso', on_delete=models.CASCADE, null=False)
    primer_nombre = models.CharField(max_length=30,null=False)
    apellido_paterno = models.CharField(max_length=30,null=False)
    apellido_materno = models.CharField(max_length=30,null=True)
    moras_atraso = models.IntegerField(null=False)
    cantidad_pedidos_fiados = models.IntegerField(null=False)
    fecha_integracion_cliente = models.DateField()

    def __str__(self):
        return str(self.numero_ficha, self.rut_cliente_moroso)

class Pago_Cliente_Moroso(models.Model):
    num_pago = models.IntegerField(primary_key=True, null=False, unique=True)
    numero_ficha = models.ForeignKey('Ficha_Cliente_Moroso', on_delete=models.DO_NOTHING, null=False)
    rut_cliente_moroso = models.ForeignKey('Cliente_Moroso', on_delete=models.DO_NOTHING, null=False)
    primer_nombre = models.CharField(max_length=30,null=False)
    apellido_paterno = models.CharField(max_length=30,null=False)
    fecha_abono = models.DateField(null=False)
    monto_abono = models.IntegerField(null=False)
    monto_total = models.IntegerField(null=False)
    codigo_boleta = models.ForeignKey('Boleta',on_delete=models.DO_NOTHING, null=False)

    def __str__(self):
        return str(self.num_pago, self.monto_total)
