from django.contrib import admin

# Register your models here.

from .models import Cliente, Proveedor, Articulos
admin.site.register(Cliente)
admin.site.register(Proveedor)
admin.site.register(Articulos)