# Generated by Django 4.2.6 on 2023-11-22 13:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aplic', '0019_remove_cliente_last_login_remove_cliente_password_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='cliente',
            name='is_staff',
        ),
    ]
