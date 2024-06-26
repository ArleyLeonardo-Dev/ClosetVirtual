# Generated by Django 5.0.4 on 2024-04-08 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Camisas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('color', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Combinaciones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Zapatos', models.CharField(max_length=100)),
                ('PantalonesFaldas', models.CharField(max_length=100)),
                ('Camisas', models.CharField(max_length=100)),
                ('Vestidos', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='PantalonesFaldas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('color', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Vestidos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('color', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Zapatos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('color', models.CharField(max_length=100)),
            ],
        ),
    ]
