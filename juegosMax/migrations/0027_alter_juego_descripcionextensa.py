# Generated by Django 5.0.6 on 2024-06-22 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('juegosMax', '0026_alter_imagen_options_imagen_orden'),
    ]

    operations = [
        migrations.AlterField(
            model_name='juego',
            name='descripcionExtensa',
            field=models.CharField(max_length=1000),
        ),
    ]