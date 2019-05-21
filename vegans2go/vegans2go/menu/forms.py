from .models import Categoria
from django import forms


class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nome', 'descricao']
