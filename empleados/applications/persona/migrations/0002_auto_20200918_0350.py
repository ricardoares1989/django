# Generated by Django 3.1.1 on 2020-09-18 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Habilidades',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('habilidad', models.CharField(max_length=30, verbose_name='Habilidad')),
            ],
            options={
                'verbose_name': 'Habilidad del empleado',
                'verbose_name_plural': 'Habilidades del empleado',
                'ordering': ['habilidad'],
            },
        ),
        migrations.AlterModelOptions(
            name='empleado',
            options={'ordering': ['first_name'], 'verbose_name': 'Empleado de ideartec', 'verbose_name_plural': 'Empleados de ideartec'},
        ),
    ]
