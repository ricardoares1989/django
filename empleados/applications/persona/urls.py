from django.urls import path
from . import views


urlpatterns = [
    path('listar-empleados', views.ListAllEmpleados.as_view()),
    path('listar-by-area/<short_name>', views.ListaByAreaEmpleado.as_view()),
]
