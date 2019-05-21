from django.shortcuts import render, redirect
from .models import Categoria, Produto
from .forms import CategoriaForm


# Create your views here.
def menu(request):
    produtos = Produto.objects.all()
    context = {
        "produtos": produtos
    }
    # for produto in produtos:
    #     print(produto.image.url)
    return render(request, 'menu.html', context)


def categoria(request):
    categorias = Categoria.objects.all()

    context = {
        'categorias': categorias
    }

    return render(request, 'categoria.html', context)


def criar_categoria(request):
    form = CategoriaForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('categoria')

    context = {
        'form': form
    }

    return render(request, 'criar_categoria.html', context)


def editar_categoria(request, id):
    categoriaEditada = Categoria.objects.get(id=id)
    form = CategoriaForm(request.POST or None, instance=categoriaEditada)

    if form.is_valid():
        form.save()
        return redirect('categoria')

    context = {
        'form': form,
        'categoriaEditada': categoriaEditada
    }

    return render(request, 'criar_categoria.html', context)


def deletar_categoria(request, id):
    categoriaEditada = Categoria.objects.get(id=id)

    if request.method == 'POST':
        categoriaEditada.delete()
        return redirect('categoria')

    context = {
        'elementoDeletado': categoriaEditada
    }

    return render(request, 'confirmar_delete_categoria.html', context)
