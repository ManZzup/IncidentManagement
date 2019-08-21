# Generated by Django 2.2.1 on 2019-08-14 04:53

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('incidents', '0026_auto_20190814_0441'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incidentseverity',
            name='current_severity',
            field=models.PositiveIntegerField(default='10', validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)]),
        ),
        migrations.AlterField(
            model_name='incidentseverity',
            name='previous_severity',
            field=models.PositiveIntegerField(default='10', validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)]),
        ),
    ]
