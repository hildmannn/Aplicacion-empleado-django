from django import forms

class newDepartament (forms.Form):
    nombre = forms.CharField( max_length=50)
    apellido = forms.CharField( max_length=50)
    departamento = forms.CharField( max_length=50)
    shorName = forms.CharField( max_length=50)