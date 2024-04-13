from django.db import models

# Create your models here.
class Zapatos(models.Model):
    nombre = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    

class PantalonesFaldas(models.Model):
    nombre = models.CharField(max_length=100)
    color = models.CharField(max_length=100)


class Camisas(models.Model):
    nombre = models.CharField(max_length=100)
    color = models.CharField(max_length=100)


class Vestidos(models.Model):
    nombre = models.CharField(max_length=100)
    color = models.CharField(max_length=100)

class Combinaciones(models.Model):
    Zapatos = models.CharField(max_length=100)
    PantalonesFaldas = models.CharField(max_length=100, null=True)
    Camisas = models.CharField(max_length=100, null=True)
    Vestidos = models.CharField(max_length=100, null=True)

