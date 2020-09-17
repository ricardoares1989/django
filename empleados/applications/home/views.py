from django.shortcuts import render
from django.views.generic import TemplateView, ListView

# Create your views here.
class PruebaView(TemplateView):
    """ Vista generica."""
    # vamos a referenciar el template que pintaremos.
    template_name = 'home/prueba.html'


class PruebaListView(ListView):
    template_name = "home/list.html"
    queryset = [n for n in range(10)]
    context_object_name = 'lista_numeros'
