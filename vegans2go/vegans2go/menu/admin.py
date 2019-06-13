from django.contrib import admin
from .models import Categoria
from .models import Produto


# Register your models here.
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'valor', 'status', 'categoria', 'descricao']
    search_fields = ['nome', 'categoria']


admin.site.register(Produto, ProdutoAdmin)


class CatedoriaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'descricao']
    search_fields = ['nome']


# Categoria
admin.site.register(Categoria, CatedoriaAdmin)
