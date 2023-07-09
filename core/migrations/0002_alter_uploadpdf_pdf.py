# Generated by Django 4.2.3 on 2023-07-08 09:11

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadpdf',
            name='pdf',
            field=models.FileField(upload_to='pdf/', validators=[django.core.validators.FileExtensionValidator(['pdf'])]),
        ),
    ]
