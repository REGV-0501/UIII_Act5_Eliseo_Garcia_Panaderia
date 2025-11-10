# app_Panaderia/admin.py
from django.contrib import admin
from .models import Ingrediente, Receta, Producto # Importar Producto

@admin.register(Ingrediente)
class IngredienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'unidad_medida', 'costo_unitario', 'proveedor', 'fecha_compra', 'stock_disponible')
    search_fields = ('nombre', 'proveedor')
    list_filter = ('unidad_medida', 'proveedor', 'fecha_compra')
    date_hierarchy = 'fecha_compra'

@admin.register(Receta)
class RecetaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'tiempo_preparacion', 'autor', 'fecha_creacion')
    search_fields = ('nombre', 'autor')
    list_filter = ('autor', 'fecha_creacion')
    date_hierarchy = 'fecha_creacion'
    filter_horizontal = ('ingredientes',)

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio_venta', 'receta', 'fecha_elaboracion', 'fecha_vencimiento')
    search_fields = ('nombre', 'receta__nombre') # Permite buscar por el nombre de la receta
    list_filter = ('receta', 'fecha_elaboracion', 'fecha_vencimiento')
    date_hierarchy = 'fecha_elaboracion'
    # Campos que se pueden editar directamente en la vista de lista
    list_editable = ('precio_venta',)