# app_Panaderia/models.py
from django.db import models

# ==========================================
# MODELO: Ingrediente (EXISTENTE)
# ==========================================
class Ingrediente(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    unidad_medida = models.CharField(max_length=50)
    costo_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    proveedor = models.CharField(max_length=100, blank=True, null=True)
    fecha_compra = models.DateField()
    stock_disponible = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return self.nombre
    class Meta:
        verbose_name = "Ingrediente"
        verbose_name_plural = "Ingredientes"
# ==========================================

# ==========================================
# MODELO: Receta (EXISTENTE)
# ==========================================
class Receta(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    tiempo_preparacion = models.IntegerField(help_text="Tiempo en minutos")
    fecha_creacion = models.DateField()
    autor = models.CharField(max_length=100)
    ingredientes = models.ManyToManyField(Ingrediente, related_name='recetas')

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Receta"
        verbose_name_plural = "Recetas"
# ==========================================

# ==========================================
# MODELO: Producto (AHORA ACTIVO)
# ==========================================
class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    precio_venta = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_elaboracion = models.DateField()
    fecha_vencimiento = models.DateField()
    receta = models.ForeignKey(Receta, on_delete=models.CASCADE, related_name='productos')
    def __str__(self):
        return f"{self.nombre} (${self.precio_venta})"
    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"