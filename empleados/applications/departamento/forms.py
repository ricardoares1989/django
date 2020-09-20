from django import forms

class NewDepartamentForm(forms.Form):
    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)
    departament = forms.CharField(max_length=50)
    short_name = forms.CharField(max_length=20)
    
