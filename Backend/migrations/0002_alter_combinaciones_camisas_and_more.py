# Generated by Django 5.0.4 on 2024-04-09 02:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Backend', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='combinaciones',
            name='Camisas',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AlterField(
            model_name='combinaciones',
            name='PantalonesFaldas',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AlterField(
            model_name='combinaciones',
            name='Vestidos',
            field=models.CharField(default=None, max_length=100),
        ),
    ]
