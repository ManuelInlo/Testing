# Generated by Django 3.0.5 on 2020-04-25 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('candidates', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate',
            name='email',
            field=models.EmailField(default='none@something.com', max_length=254),
        ),
    ]
