# Generated by Django 3.0.5 on 2020-04-22 16:24

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ppco2', '0005_auto_20200422_2321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calculation',
            name='e3',
            field=models.PositiveSmallIntegerField(default=1, verbose_name='Q4 - How many people do you share your living space and your electricity bill with (family or roommates living in the same space)?'),
        ),
        migrations.AlterField(
            model_name='calculation',
            name='e4',
            field=models.PositiveSmallIntegerField(default=8, validators=[django.core.validators.MaxValueValidator(24), django.core.validators.MinValueValidator(0)], verbose_name='Q5 - How many hours per day do you spend in air-conditioning outside of your home (e.g. office, coffee shop)'),
        ),
        migrations.AlterField(
            model_name='calculation',
            name='e5',
            field=models.PositiveSmallIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1)], verbose_name='Q6 - Roughly how many people share this in total (including yourself. E.g. crowded coffee shop with 20 people, or small office with 4 people)?'),
        ),
        migrations.AlterField(
            model_name='calculation',
            name='e6',
            field=models.PositiveSmallIntegerField(default=800, validators=[django.core.validators.MinValueValidator(500), django.core.validators.MaxValueValidator(4000)], verbose_name='Q3 - What rate do you pay for electricity? (KHR/kWh)'),
        ),
    ]
