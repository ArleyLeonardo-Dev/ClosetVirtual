# Generated by Django 5.0.4 on 2024-04-09 03:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Backend', '0002_alter_combinaciones_camisas_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='combinaciones',
            name='Camisas',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='combinaciones',
            name='PantalonesFaldas',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='combinaciones',
            name='Vestidos',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
