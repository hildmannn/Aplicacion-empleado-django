from django import forms
from .models import Empleado

class EmpleadoForm(forms.ModelForm):

    class Meta:
        model = Empleado
        fields = ('first_name',
                  'last_name',
                  'job',
                  'departamento',
                  'imagen',
                  'habilidades',
            )
        widgets = {
            'habilidades': forms.CheckboxSelectMultiple()
        }

