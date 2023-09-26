# Generated by Django 4.2.5 on 2023-09-26 23:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplic', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cartao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.CharField(max_length=12, verbose_name='Número Cartão')),
                ('senha', models.CharField(max_length=200, verbose_name='Senha Cartão')),
            ],
            options={
                'verbose_name': 'Cartão',
                'verbose_name_plural': 'Cartões',
            },
        ),
    ]
