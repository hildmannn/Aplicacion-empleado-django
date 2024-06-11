from django.urls import path
from . import views

app_name = 'persona_app'


urlpatterns = [
 #----------------- URLS DE MI PRIMER PROYECTO --------------------------------------------------------------------------------------------------------------   
     path('/', 
         views.inicio.as_view(),
         name= 'inicio'
    ),
     path('allViews/',
           views.AllViews.as_view(),
           name= 'listarEmpleados'
     ),
     path('detalles_empleado/<int:pk>',
           views.DetailViewEmpleado.as_view(),
           name= 'detalles_empleado'
     ),
     path('AllViewsByArea/<shortName>/', 
          views.AllViewsByArea.as_view(),
          name='EmpleadosPorArea'
     ),
     path('allViewsAdmin/',
           views.AllViewsAdmin.as_view(),
           name= 'viewsAdmin'
     ),
     path('updeteFormulario/<pk>', 
         views.formularioUpdateView.as_view(),
         name= 'update'
    ),
     path('deleteEmpleado/<pk>', 
         views.empleadoDeleteView.as_view(),
         name= 'delete'
    ),
     path('crear-usuario/',
           views.EmpleadoCreateView.as_view(),
           name='CrearUsuario'
     ),

#----------------- URLS DE PRUEBAS --------------------------------------------------------------------------------------------------------------
    
    
    path('buscar-empleado/', views.byKword.as_view()),
    path('buscar-habilidades/', views.findByHabilidades.as_view()),
   
    path('succes/', 
         views.successTemplate.as_view(),
         name= 'correcto'
    ),
 
   
]