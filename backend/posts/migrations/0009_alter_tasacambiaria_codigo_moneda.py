# Generated by Django 4.0.6 on 2023-11-22 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0008_remove_historialcrediticio_visitas_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasacambiaria',
            name='codigo_moneda',
            field=models.CharField(max_length=3, unique=True),
        ),
    ]
