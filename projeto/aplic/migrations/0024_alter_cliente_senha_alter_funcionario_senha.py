# Generated by Django 4.2.5 on 2023-10-03 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplic', '0023_alter_cartao_options_alter_endereco_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='senha',
            field=models.CharField(max_length=100, verbose_name='Senha'),
        ),
        migrations.AlterField(
            model_name='funcionario',
            name='senha',
            field=models.CharField(max_length=100, verbose_name='Senha'),
        ),
    ]
