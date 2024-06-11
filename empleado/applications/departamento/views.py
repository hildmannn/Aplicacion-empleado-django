from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView,CreateView,ListView
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from .forms import newDepartament
from .models import departamento
from applications.persona.models import Empleado
# Create your views here.
#----------------- VIEWS DE MI PRIMER PROYECTO --------------------------------------------------------------------------------------------------------------
class DepartamentosListView(ListView):
    model = departamento
    template_name = "departamento/listAllDepartamentos.html"

class departamentoFormView(FormView):     #Form view es una vista que simula un formulario que puede servir para hacer un createView con mas de un modelo
    template_name = "departamento/addDepartamento.html"
    form_class = newDepartament
    success_url = reverse_lazy('departamento_app:ListarDepartamentos')



    def form_valid(self, form: BaseModelForm) -> HttpResponse:

        depa = departamento(                  #aca llamamos el modelo departamento y le asignamos un campo del formulario creado en forms.py
            name= form.cleaned_data['departamento'],
            short_name= form.cleaned_data['shorName']
        )       
        depa.save()    #aca guardamos la variable depa en la base de datos para que podamos hacer la relacion con el empleado 
        
        nombre = form.cleaned_data['nombre']     #aca asignamos de nuevo el nombre y apellido del empleado en una variable
        apellido = form.cleaned_data['apellido']
        Empleado.objects.create(              #aca hacemos la relacion del forms y la conectamos con el modelo de persona y de departamento
            first_name = nombre,
            last_name = apellido,
            job = '1',
            departamento = depa
        )
        

        return super(departamentoFormView, self).form_valid(form)


#----------------- VIEWS DE PRUEBAS --------------------------------------------------------------------------------------------------------------
class indexView(TemplateView):
    template_name = "departamento/index.html"






