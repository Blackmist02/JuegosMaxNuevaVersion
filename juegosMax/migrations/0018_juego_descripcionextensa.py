# Generated by Django 5.0.6 on 2024-06-15 01:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('juegosMax', '0017_juego_precio'),
    ]

    operations = [
        migrations.AddField(
            model_name='juego',
            name='descripcionExtensa',
            field=models.CharField(default=1, max_length=500),
            preserve_default=False,
        ),
    ]