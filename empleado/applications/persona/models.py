from django.db import models
from applications.departamento.models import departamento

# Create your models here.

class habilidades(models.Model):
    habilidades = models.CharField("Habilidad", max_length=50)
    
    class Meta:
        verbose_name= 'habilidad'
        verbose_name_plural = 'Habilidades Empleado'
    
    def __str__(self):
        return self.habilidades 

class Empleado (models.Model):
    """Modelo para tabla empleado"""

    JOB_CHOICES = (
        ('0','CONTADOR'),
        ('1','ADMINISTRADOR'),
        ('2','ECONOMISTA'),
        ('0','OTRO'),
    )

    first_name = models.CharField("nombre", max_length=50)
    last_name = models.CharField("apellidos", max_length=50)
    full_name = models.CharField("nombre_completo", max_length=100, blank=True)
    job = models.CharField("trabajo", max_length=1, choices=JOB_CHOICES)
    departamento = models.ForeignKey(departamento, on_delete=models.CASCADE)
    imagen = models.ImageField("imagen", upload_to=None, height_field=None, width_field=None, max_length=None, null=True)
    habilidades = models.ManyToManyField(habilidades)

    def __str__(self):
        return str(self.id) + "-" + self.first_name + "-" + self.last_name
