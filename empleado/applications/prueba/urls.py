from django.urls import path, include
from . import views



app_name = 'prueba_app'

urlpatterns = [
    path("prueba/",views.pruebaView.as_view() ),
    path("pruebaLista/",views.listViewPrueba.as_view() ),
    path("pruebaListaModels/",views.ListaViewModel.as_view() ),
    path("addPrueba/",
         views.addPrueba.as_view(),
         name='addPrueba'),
    ]