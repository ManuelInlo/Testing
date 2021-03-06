# Generated by Django 3.0.5 on 2020-06-20 15:26

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('candidates', '0006_auto_20200523_1053'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate',
            name='created_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='candidate',
            name='status',
            field=models.CharField(choices=[('AVAILABLE', 'AVAILABLE'), ('INTERVIEW', 'INTERVIEW'), ('NOT AVAILABLE', 'NOT AVAILABLE'), ('HIRED', 'HIRED')], default='AVAILABLE', max_length=200),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='source',
            field=models.CharField(choices=[('SELECIONAR', 'SELECIONAR'), ('Bolsa de trabajo UV', 'Bolsa de trabajo UV'), ('OCC Mundial', 'OCC Mundial'), ('Buscotrabajo', 'Buscotrabajo'), ('Quierotrabajo', 'Quierotrabajo')], default='SELECCIONAR', max_length=200),
        ),
    ]
