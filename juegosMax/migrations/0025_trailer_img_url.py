# Generated by Django 5.0.6 on 2024-06-21 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('juegosMax', '0024_juego_precio'),
    ]

    operations = [
        migrations.AddField(
            model_name='trailer',
            name='img_url',
            field=models.URLField(default=''),
        ),
    ]
