# Generated by Django 3.0.5 on 2020-05-23 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('candidates', '0004_auto_20200523_1035'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate',
            name='recruiter',
            field=models.IntegerField(choices=[(0, 'SELEECIONAR'), (1, 'Freddy Iniguez'), (2, 'Manuel Iniguez'), (3, 'Juan Perez')], default=0),
        ),
    ]
