# Generated by Django 5.0.4 on 2024-05-07 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0002_habilidades_empleado_habilidades'),
    ]

    operations = [
        migrations.AddField(
            model_name='empleado',
            name='full_name',
            field=models.CharField(blank=True, max_length=50, verbose_name='nombre_completo'),
        ),
    ]