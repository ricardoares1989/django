from django.urls import path

from . import views

urlpatterns = [
    path('prueba/', views.PruebaView.as_view()),
    path('lista/', views.PruebaListView.as_view()),
    path('lista-prueba/', views.ListarPrueba.as_view()),
    path('create/', views.PruebaCreateView.as_view(), name='prueba_create'),
    path('practica/', views.PracticaView.as_view(), name='practica'),
]
