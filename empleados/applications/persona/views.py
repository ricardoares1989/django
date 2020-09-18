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
    
    def get_queryset(self):
        """ Siempre debe retornar una lista de elementos."""
        area = self.kwargs['short_name']
        lista = Empleado.objects.filter(departament__short_name=area)
        return lista