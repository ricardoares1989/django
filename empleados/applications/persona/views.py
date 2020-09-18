from django.shortcuts import render
from django.views.generic import ListView

from .models import Empleado
# Create your views here.

class ListAllEmpleados(ListView):
    # Toda vista basada en clases requiere del template.
    template_name = 'persona/list_all.html'
    model = Empleado
    context_object_name = 'lista'

class ListaByAreaEmpleado(ListView):
    template_name = 'persona/list_by_area.html'
    model = Empleado
    queryset =  Empleado.objects.filter(departament__name='Contabilidad')
