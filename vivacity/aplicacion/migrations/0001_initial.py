# Generated by Django 4.2.7 on 2023-11-30 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255)),
                ('correo', models.EmailField(max_length=255)),
                ('contraseña', models.CharField(max_length=255)),
                ('verifica_contraseña', models.CharField(max_length=255)),
            ],
        ),
    ]
