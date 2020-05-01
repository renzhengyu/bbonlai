# Generated by Django 3.0.5 on 2020-05-01 17:57

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ppco2', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calculation',
            name='f2',
            field=models.PositiveSmallIntegerField(default=20, validators=[django.core.validators.MinValueValidator(1)], verbose_name='Q3 - How long do you think the house will be around? (in years)'),
        ),
    ]
