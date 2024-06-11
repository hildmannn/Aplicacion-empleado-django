from .models import addPrueba
from django import forms


class pruebaForm(forms.ModelForm):
    
    class Meta:
        model = addPrueba
        fields = ('titulo',
                  'subtitulo',
                  'cantidad')
        
        widgets = {
            'titulo':forms.TextInput(
                {'placeholder' : 'ingrese el nombre'}
            )
        }
    
    def clean_cantidad(self):
        cantidad = self.cleaned_data.get('cantidad')

        if cantidad <=10:
            raise forms.ValidationError('Ingrese un numero mayor a 10')
        
        elif cantidad >20:
            raise forms.ValidationError('Ingrese un numero menos a 20')
        
        return cantidad
    

