from django.urls import path, include
from . import views

app_name = 'departamento_app'
urlpatterns = [
    #----------------- URLS DE MI PRIMER PROYECTO --------------------------------------------------------------------------------------------------------------   
    path('', 
        views.DepartamentosListView.as_view(),
        name= 'ListarDepartamentos'
    ),
    path('agregarDepartamento/',
          views.departamentoFormView.as_view(),
            name= 'addDepartamento' ),
    
    #----------------- URLS DE PRUEBAS --------------------------------------------------------------------------------------------------------------
    path('index/', views.indexView.as_view() ),
    
]
