# Generated by Django 5.0.6 on 2024-06-12 03:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('juegosMax', '0007_alter_juego_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='juego',
            name='imagen',
            field=models.ImageField(upload_to='portadas/'),
        ),
    ]