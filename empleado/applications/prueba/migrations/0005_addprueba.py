# Generated by Django 5.0.4 on 2024-05-09 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prueba', '0004_alter_departamento_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='addPrueba',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=30)),
                ('subtitulo', models.CharField(max_length=50)),
                ('cantidad', models.IntegerField()),
            ],
        ),
    ]