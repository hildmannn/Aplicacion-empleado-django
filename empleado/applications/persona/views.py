from typing import Any
from django.db.models.query import QuerySet
from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, CreateView, TemplateView, UpdateView, DeleteView, DetailView
from .models import Empleado
from django.urls import reverse_lazy
#formularios
from .forms import EmpleadoForm

# Create your views here.
#----------------- VIEWS DE MI PRIMER PROYECTO --------------------------------------------------------------------------------------------------------------


class inicio(TemplateView):
    template_name = "inicio.html"

class AllViews(ListView):
    model = Empleado
    template_name = "persona/List_all.html"
    paginate_by = 8
    def get_queryset(self):

        palabraClave = self.request.GET.get('kword','')
        empleado = Empleado.objects.filter(
            full_name__icontains = palabraClave
        )
        return empleado
    

class DetailViewEmpleado(DetailView):
    model = Empleado
    template_name = "persona/detailEmpleado.html"

class AllViewsByArea(ListView):
    model = Empleado
    template_name = "persona/byArea.html"
    paginate_by = 8
    def get_queryset(self):
        area = self.kwargs['shortName']
        lista = Empleado.objects.filter(departamento__short_name = area)
        return lista 

class AllViewsAdmin(ListView):
    model = Empleado
    template_name = "persona/List_all_admin.html"
    paginate_by = 8
    def get_queryset(self):

        palabraClave = self.request.GET.get('kword','')
        empleado = Empleado.objects.filter(
            full_name__icontains = palabraClave
        )
        return empleado
    
class formularioUpdateView(UpdateView):
    model = Empleado
    template_name = "persona/formularioUpdate.html"
    fields = ['first_name',
              'last_name',
              'job',
              'departamento',
              'habilidades',
              'imagen',
    ]
    success_url = reverse_lazy('persona_app:viewsAdmin')



class empleadoDeleteView(DeleteView):
    model = Empleado
    template_name = "persona/deleteEmpleado.html"
    success_url = reverse_lazy('persona_app:viewsAdmin')
    context_object_name = 'empleado'

class EmpleadoCreateView(CreateView):
    model = Empleado
    template_name = "persona/CreateEmpleado.html"
    form_class = EmpleadoForm
    success_url = reverse_lazy('persona_app:listarEmpleados')
    
    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        empleado = form.save( commit=False )  #guarda el formulario en una variable y el commit false es para hacer un simulado del guardado en vez de guardarlo de verdad para optimizar el programa
        empleado.full_name = empleado.first_name + ' ' + empleado.last_name
        empleado.save()

        return super(EmpleadoCreateView, self).form_valid(form)
    
    
    





#----------------- VIEWS DE PRUEBAS --------------------------------------------------------------------------------------------------------------


    

class byKword(ListView): 
    template_name = "persona/byKword.html"
    context_object_name = 'empleados'
    
    def get_queryset(self):
        palabraClave = self.request.GET.get('kword')
        empleado = Empleado.objects.filter(
            first_name = palabraClave
        )
        return empleado


class findByHabilidades(ListView):
    template_name = "persona/porHabilidades.html"
    context_object_name = 'habilidades'
    
    def get_queryset(self):
        empleadoId = Empleado.objects.get(id=1)
        return empleadoId.habilidades.all()




    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        empleado = form.save( commit=False )  #guarda el formulario en una variable y el commit false es para hacer un simulado del guardado en vez de guardarlo de verdad para optimizar el programa
        empleado.full_name = empleado.first_name + '' + empleado.last_name
        empleado.save()

        return super(EmpleadoCreateView, self).form_valid(form)

class successTemplate (TemplateView):
    template_name = "persona/success.html"


