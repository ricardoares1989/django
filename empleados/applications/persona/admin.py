from django.contrib import admin
from .models import Empleado, Habilidades

# Register your models here.

admin.site.register(Habilidades)

class EmpleadoAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'first_name',
        'last_name',
        'departament',
        'job',
        'fullname'
    )

    def fullname(self, obj):
        # obj hace referencia a cada objeto ya que en el admin itera sobre
        # todos los objetos de ese modelo.
        return obj.first_name + obj.last_name

    search_fields = (
        'first_name',
        'last_name'
    )
    list_filter = (
        'job',
        'departament'
    )
    filter_horizontal = ('habilidades',)
admin.site.register(Empleado, EmpleadoAdmin)
