from django.db import models

# Create your models here.
class Cliente(models.Model):
    nombre = models.CharField(primary_key=True,max_length=10,unique=True,validators=[validacion_numeros,MinLengthValidator(10)])# Para validar que solo ingrese numeros no letras
    direccion = models.TextField(max_length=50)
    telefono = models.CharField(max_length=10)
    email = models.EmailField()
    def __str__(self):
        return self.nombre

class Proveedor(models.Model):
    nombre = models.CharField(primary_key=True,max_length=10,unique=True)
    direccion = models.CharField(max_length=50)
    telefono = models.CharField(max_length=10)
    email = models.EmailField()
    def __str__(self):
        return self.nombre
    
        
class Articulos (models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()
    stock = models.IntegerField()
    FechaElaboracion = models.IntegerField()
    FechaVencimiento = models.IntegerField()
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre
    

