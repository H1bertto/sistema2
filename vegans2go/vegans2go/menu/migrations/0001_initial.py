# Generated by Django 2.2.1 on 2019-05-21 00:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=50)),
                ('descricao', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=100)),
                ('descricao', models.CharField(max_length=200)),
                ('valor', models.DecimalField(decimal_places=2, max_digits=5)),
                ('quantidade', models.IntegerField()),
                ('status', models.CharField(choices=[('A', 'Disponivel'), ('U', 'Indisponivel'), ('R', 'Removido')], max_length=1)),
                ('image', models.ImageField(blank=True, null=True, upload_to='menu/images', verbose_name='Imagem')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menu.Categoria')),
            ],
            options={
                'verbose_name': 'Produto',
                'verbose_name_plural': 'Produtos',
                'ordering': ['nome'],
            },
        ),
    ]
