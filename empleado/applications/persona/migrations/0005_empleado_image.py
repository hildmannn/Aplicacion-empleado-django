# Generated by Django 5.0.4 on 2024-05-22 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0004_alter_empleado_full_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='empleado',
            name='image',
            field=models.ImageField(null=True, upload_to=None, verbose_name='imagen'),
        ),
    ]
