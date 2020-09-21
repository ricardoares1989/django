
from django.urls import path

from . import views

app_name = 'departamento_app'

urlpatterns = [
    path('new-departamento/', views.NewDepartamentView.as_view(), name='nuevo_departamento'),
    path(
        'listar-departamentos/',
        views.DepartamentoListView.as_view(),
        name='listar_departamentos'
    )
]
