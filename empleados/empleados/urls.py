"""Empleados URL Configuration
"""
from django.contrib import admin
from django.urls import path, re_path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # inluimos los urls de las apps locales.
    re_path('', include('applications.home.urls')),
    re_path('', include('applications.persona.urls')),
]
