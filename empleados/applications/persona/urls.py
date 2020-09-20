from django.urls import path
from . import views

app_name = 'persona_app'

urlpatterns = [
    path('listar-empleados/', views.ListAllEmpleados.as_view()),
    path('listar-by-area/<short_name>', views.ListaByAreaEmpleado.as_view()),
    path('buscar-empleado/', views.ListEmpleadosByKWord.as_view()),
    path('lista-habilidades/', views.ListHabilidadesEmpleado.as_view()),
    path('ver-empleado/<pk>/', views.EmpleadoDetailView.as_view()),
    path('create-empleado/', views.EmpleadoCreateView.as_view()),
    path('success/', views.SuccessView.as_view(), name='success'),
    path('update/<pk>/', views.EmpleadoUpdateView.as_view(), name='update'),
    path('delete/<pk>/', views.EmpleadDeleteView.as_view(), name='delete'),
]
