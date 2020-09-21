from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    TemplateView,
    UpdateView,
    DeleteView
)
from django.urls import reverse_lazy
from .models import Empleado
# Create your views here.
from .forms import EmpleadoForm

class InicioView(TemplateView):
    """ Vista que carga la pagina de inicio."""
    template_name = 'inicio.html'

class ListAllEmpleados(ListView):
    # Toda vista basada en clases requiere del template.
    template_name = 'persona/list_all.html'
    paginate_by = 4
    ordering = ['first_name']
    model = Empleado
    context_object_name = 'lista'
    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword", '')
        if palabra_clave:
            lista = Empleado.objects.filter(
                fullname__icontains=palabra_clave
            )
        else:
            lista = Empleado.objects.all()
        return lista


class ListarEmpleados(ListView):
    # Toda vista basada en clases requiere del template.
    template_name = 'persona/list_empleados.html'
    paginate_by = 4
    ordering = ['first_name']
    model = Empleado
    context_object_name = 'empleados'


class ListaByAreaEmpleado(ListView):
    template_name = 'persona/list_by_area.html'
    model = Empleado
    context_object_name = 'empleados'
    paginate_by = 4
    def get_queryset(self):
        """ Siempre debe retornar una lista de elementos."""
        area = self.kwargs['short_name']
        lista = Empleado.objects.filter(departament__short_name=area)
        return lista

class ListEmpleadosByKWord(ListView):
    """ Lista empleados por palabra clave."""
    template_name = 'persona/by_kword.html'
    context_object_name = 'empleados'
    #Nombre para referirte al objeto en el template.
    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword", '')
        lista = Empleado.objects.filter(first_name=palabra_clave)
        return lista

class ListHabilidadesEmpleado(ListView):
    template_name = 'persona/habilidades.html'
    context_object_name = 'habilidades'
    
    def get_queryset(self):
        empleado = Empleado.objects.get(id=12)
        habilidades = empleado.habilidades.all()
        return habilidades

class EmpleadoDetailView(DetailView):
    model = Empleado
    template_name = "persona/detail_empleado.html"

    def get_context_data(self, **kwargs):
        context = super(EmpleadoDetailView, self).get_context_data(**kwargs)
        context["titulo"] = "Empleado del mes" 
        return context

class SuccessView(TemplateView):
    template_name = 'persona/success.html'

class EmpleadoCreateView(CreateView):
    model = Empleado
    template_name = "persona/add.html"
    form_class = EmpleadoForm
    success_url = reverse_lazy('persona_app:empleados_crud')

    def form_valid(self, form):
        # Estoy salvando lo que esta en form en la base de datos.
        empleado = form.save(commit=False)
        empleado.fullname = empleado.first_name + ' ' + empleado.last_name
        empleado.save()
        return super(EmpleadoCreateView, self).form_valid(form)
    
class EmpleadoUpdateView(UpdateView):
    model = Empleado
    template_name = "persona/update-empleado.html"
    fields = '__all__'
    success_url = reverse_lazy('persona_app:empleados_crud')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        request.POST['last_name']
        return super(EmpleadoUpdateView, self).post(request, *args, **kwargs)

    def form_valid(self, form):
        return super(EmpleadoUpdateView, self).form_valid(form)

class EmpleadDeleteView(DeleteView):
    model = Empleado
    template_name = "persona/delete-view.html"
    success_url = reverse_lazy('persona_app:empleados_crud')
    