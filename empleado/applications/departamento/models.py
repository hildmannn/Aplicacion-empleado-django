from django.db import models

# Create your models here.

class departamento (models.Model):
    name = models.CharField("nombre", max_length=50, unique=True)
    short_name = models.CharField("nombre corto", max_length=50, unique=True)
    active = models.BooleanField("activo", default=False)

    def __str__(self):
        return str(self.id) + "-" + self.name + "-" + self.short_name