from django.urls import path
from . import views

app_name = 'persona_app'

urlpatterns = [
    path('', views.InicioView.as_view()),
    path(
        'listar-empleados/',
        views.ListAllEmpleados.as_view(),
        name='empleados_all'
    ),
    path(
        'listar-empleados-crud/',
        views.ListarEmpleados.as_view(),
        name='empleados_crud'
    ),
    path(
        'listar-by-area/<short_name>',
        views.ListaByAreaEmpleado.as_view(),
        name='area_detail'    
    ),
    path('buscar-empleado/', views.ListEmpleadosByKWord.as_view()),
    path('lista-habilidades/', views.ListHabilidadesEmpleado.as_view()),
    path(
        'ver-empleado/<pk>/',
        views.EmpleadoDetailView.as_view(),
        name="empleado_detail"
    ),
    path(
        'create-empleado/',
        views.EmpleadoCreateView.as_view(),
        name="empleado_add"
    ),
    path('success/', views.SuccessView.as_view(), name='success'),
    path('update/<pk>/', views.EmpleadoUpdateView.as_view(), name='update'),
    path('delete/<pk>/', views.EmpleadDeleteView.as_view(), name='delete'),
]
