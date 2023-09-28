# Generated by Django 4.2.5 on 2023-09-28 00:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplic', '0004_alter_funcionario_salario'),
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('preco', models.DecimalField(decimal_places=2, max_digits=8, null=True, verbose_name='Preço')),
                ('peso', models.DecimalField(decimal_places=2, max_digits=8, null=True, verbose_name='Peso')),
                ('marca', models.CharField(max_length=50, verbose_name='Nome da Marca')),
                ('_estoque', models.IntegerField(verbose_name='Número Cartão')),
                ('nome_produto', models.CharField(max_length=50, verbose_name='Nome da Marca')),
            ],
            options={
                'verbose_name': 'Produto',
                'verbose_name_plural': 'Produtos',
            },
        ),
    ]
