from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView
from .models import pruebaModel,addPrueba
from django.urls import reverse_lazy
from .forms import pruebaForm
# Create your views here.


class pruebaView(TemplateView):
    template_name = "prueba/prueba.html"


class listViewPrueba(ListView):
    template_name = "prueba/listaPrueba.html"
    queryset = ['A','B','C']
    context_object_name = 'listaPrueba'


class ListaViewModel(ListView):
    model = pruebaModel
    template_name = "prueba/listaPrueba.html"
    context_object_name = 'listaDesdeModel'



class addPrueba(CreateView):
    model = addPrueba
    template_name = "prueba/addPrueba.html"
    form_class = pruebaForm
    success_url = reverse_lazy('prueba_app:addPrueba')

