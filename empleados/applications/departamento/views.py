from django.shortcuts import render
from django.views.generic.edit import FormView

from .forms import NewDepartamentForm
from applications.persona.models import Empleado
from applications.departamento.models import Departamento
# Create your views here.
class NewDepartamentView(FormView):
    template_name = 'departamento/new_departamento.html'
    form_class = NewDepartamentForm
    success_url = '/'

    def form_valid(self, form):
        departament = form.cleaned_data['departament']
        short_name = form.cleaned_data['short_name']
        depa = Departamento.objects.create(
            name=departament,
            short_name=short_name
        )
        depa.save()
        nombre = form.cleaned_data['nombre']
        apellido = form.cleaned_data['apellido']
        Empleado.objects.create(
            first_name=nombre,
            last_name=apellido,
            job=1,
            departament=depa,
        )
        return super(NewDepartamentView, self).form_valid(form)