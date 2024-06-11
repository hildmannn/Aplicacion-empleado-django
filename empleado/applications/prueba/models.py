from django.db import models

# Create your models here.
class pruebaModel(models.Model):
    titulo = models.CharField(max_length=30)
    subtitulo = models.CharField(max_length=50)
    
class departamento(models.Model):
    name = models.CharField('nombre', max_length=50, null=True, unique=True)
    shortName = models.CharField("nombre corto", max_length=50, blank=True, editable=False) #editable es para q en el admin no se puede escribir
    activo = models.BooleanField('anulado',default= False)

    class Meta:
        verbose_name= 'Mi prueba'
        verbose_name_plural = 'Area de prueba'
        ordering = ['-name']
        unique_together = ['name' , 'shortName']
    
    def __str__(self):
        return str(self.id) + '-' + self.name + '-' + self.shortName
    
class addPrueba(models.Model):
    titulo = models.CharField(max_length=30)
    subtitulo = models.CharField(max_length=50)
    cantidad = models.IntegerField()

    def __str__(self):
        return self.titulo + ' ' + self.subtitulo  + ' ' + str(self.cantidad)