# Generated by Django 3.0.2 on 2020-01-27 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banco_proyectos', '0002_residente_usuario'),
    ]

    operations = [
        migrations.AddField(
            model_name='residente',
            name='nombre',
            field=models.CharField(default=None, max_length=50),
            preserve_default=False,
        ),
    ]
