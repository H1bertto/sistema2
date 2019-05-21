from django.db import models


# Create your models here.
class CategoriaManager(models.Manager):
    def search(self, query):
        return self.get_queryset().filter(models.Q(name__icontains=query) or models.Q(description__icontains=query))


class Categoria(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=50)
    descricao = models.CharField(max_length=200)

    objects = CategoriaManager()


class ProdutoManager(models.Manager):
    def search(self, query):
        return self.get_queryset().filter(models.Q(name__icontains=query) or models.Q(description__icontains=query))


class Produto(models.Model):
    STATUS = (
        ('A', 'Disponivel'),
        ('U', 'Indisponivel'),
        ('R', 'Removido'),
    )
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=200)
    valor = models.DecimalField(max_digits=5, decimal_places=2)
    quantidade = models.IntegerField()
    status = models.CharField(max_length=1, choices=STATUS)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='menu/images', verbose_name='Imagem', null=True, blank=True)

    objects = ProdutoManager()

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'
        ordering = ['nome']
