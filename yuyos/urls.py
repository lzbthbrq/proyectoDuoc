from django.urls import path, re_path
from .views import index, Registro_pago_cm,Registro_producto
from . import views
 
urlpatterns = [ 
    path('',index,name='index'),
    path('Registro_pago_cm',Registro_pago_cm,name='Registro_pago_cm'),
    path('Registro_producto',Registro_producto,name='Registro_producto')
] 
