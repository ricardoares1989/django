from django.db import models
from applications.departamento.models import Departamento
from ckeditor.fields import RichTextField
# Create your models here.

class Habilidades(models.Model):
    """ Habilidades por empleado."""
    habilidad = models.CharField('Habilidad', max_length=30)

    class Meta:
        verbose_name = 'Habilidad del empleado'
        verbose_name_plural = 'Habilidades del empleado'
        ordering = ['habilidad']
        

    def __str__(self):
        return str(self.id) + '-' + self.habilidad


class Empleado(models.Model):
    """ Model to represent a journer"""
    JOB_CHOICES = [
        ('0', 'Contador'),
        ('1', 'Administrador'),
        ('2', 'Economista'),
        ('3', 'Abogado'),
        ('4', 'Ingeniero'),
    ]
    # Lo que se guarda en la base de datos es el numero no el descriptivo
    # asi se ahorra memoria en la base de datos.
    departament = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    first_name = models.CharField('Nombres', max_length=60)
    last_name = models.CharField('Apellidos', max_length=60)
    fullname = models.CharField("Nombre completo", max_length=120, blank=True)
    job = models.CharField('Trabajo', choices=JOB_CHOICES, max_length=50)
    avatar = models.ImageField(upload_to='empleado', blank=True, null=True)
    habilidades = models.ManyToManyField(Habilidades)
    hoja_vida = RichTextField()

    class Meta:
        verbose_name = 'Empleado de ideartec'
        verbose_name_plural = 'Empleados de ideartec'
        ordering = ['first_name']

    def __str__(self):
        return str(self.id) + '-' + self.first_name + '-' + self.last_name
    

