# Generated by Django 4.2.6 on 2023-10-30 23:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_alter_historialcrediticio_visitas_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='historialcrediticio',
            name='visitas',
        ),
        migrations.RemoveField(
            model_name='indiceinflacion',
            name='visitas',
        ),
        migrations.RemoveField(
            model_name='saludfinanciera',
            name='visitas',
        ),
        migrations.RemoveField(
            model_name='tasacambiaria',
            name='visitas',
        ),
        migrations.DeleteModel(
            name='VisitasModel',
        ),
    ]
