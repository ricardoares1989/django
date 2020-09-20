from django import forms

from .models import Prueba

class PruebaForm(forms.ModelForm):
    
    class Meta:
        model = Prueba
        fields = (
        "titulo",
        'subtitulo',
        'cantidad'
        )
        widgets ={
            'cantidad': forms.NumberInput(
                attrs={
                    'placeholder': 'Ingrese texto.',
                    "name": "cantidad",
                    "class": 'number-button'
                    }
            )
        }

    def clean_cantidad(self):
        cantidad = self.cleaned_data['cantidad']
        if cantidad < 10:
            raise forms.ValidationError('Ingrese un numero mayor a 10')
        return cantidad

