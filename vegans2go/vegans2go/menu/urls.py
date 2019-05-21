from django.urls import path
from .views import *

urlpatterns = [
    path('', menu, name='cardapio'),

    # Manipular Categorias. TODO: FALTA O LAYOUT.
    path('categoria/', categoria, name='categoria'),
    path('criar-categoria/', criar_categoria, name='criar_categoria'),
    path('editar-categoria/<int:id>/', editar_categoria, name='editar_categoria'),
    path('deletar-categoria/<int:id>/', deletar_categoria, name='deletar_categoria'),
    # -------------------------------------------------------------------------------------
]
