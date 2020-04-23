# Generated by Django 3.0.5 on 2020-04-23 08:25

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ppco2', '0008_calculation_offset'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calculation',
            name='a1',
            field=models.PositiveIntegerField(default=5000, verbose_name='Q1 - In the last 12 months, how far have you flown by plane? (km)'),
        ),
        migrations.AlterField(
            model_name='calculation',
            name='a2',
            field=models.PositiveIntegerField(default=100, verbose_name='Q2 - by train? (km)'),
        ),
        migrations.AlterField(
            model_name='calculation',
            name='a3',
            field=models.PositiveIntegerField(default=1000, verbose_name='Q3 - by bus? (km)'),
        ),
        migrations.AlterField(
            model_name='calculation',
            name='a4',
            field=models.PositiveIntegerField(default=5000, verbose_name='Q4 - by car? (km)'),
        ),
        migrations.AlterField(
            model_name='calculation',
            name='a5',
            field=models.PositiveIntegerField(default=5000, verbose_name='Q5 - by moto? (km)'),
        ),
        migrations.AlterField(
            model_name='calculation',
            name='b1',
            field=models.PositiveSmallIntegerField(default=120, help_text='(e.g. socks, undies...)', verbose_name='Q1 - In the last 12 months, how many SMALL items have you purchased?'),
        ),
        migrations.AlterField(
            model_name='calculation',
            name='b2',
            field=models.PositiveSmallIntegerField(default=48, help_text='(e.g. t-shirts, dresses...)', verbose_name='Q2 - MEDIUM-sized items?'),
        ),
        migrations.AlterField(
            model_name='calculation',
            name='b3',
            field=models.PositiveSmallIntegerField(default=6, help_text='(e.g. jeans, coats...)', verbose_name='Q3 - LARGE items?'),
        ),
        migrations.AlterField(
            model_name='calculation',
            name='c1',
            field=models.PositiveSmallIntegerField(default=10, help_text='(e.g. earphones, computer mouse...)', verbose_name='Q1 - How many VERY SMALL appliances have you purchased in the last 12 months?'),
        ),
        migrations.AlterField(
            model_name='calculation',
            name='c3',
            field=models.PositiveSmallIntegerField(default=10, help_text='(e.g. kettle, toaster, iron, speakers...)', verbose_name='Q3 - SMALL household appliances?'),
        ),
        migrations.AlterField(
            model_name='calculation',
            name='c5',
            field=models.PositiveSmallIntegerField(default=20, help_text='(e.g. laptop, monitor, small fridge, desktop computer...)', verbose_name='Q5 - MEDIUM-sized appliances?'),
        ),
        migrations.AlterField(
            model_name='calculation',
            name='c7',
            field=models.PositiveSmallIntegerField(default=10, help_text='(e.g. washing machine, large fridge...)', verbose_name='Q7 - LARGE appliances?'),
        ),
        migrations.AlterField(
            model_name='calculation',
            name='d1',
            field=models.PositiveSmallIntegerField(default=200, verbose_name='Q1 - How many grams of BEEF do you eat per week?'),
        ),
        migrations.AlterField(
            model_name='calculation',
            name='d2',
            field=models.PositiveSmallIntegerField(default=200, verbose_name='Q2 - PORK? (gram)'),
        ),
        migrations.AlterField(
            model_name='calculation',
            name='d3',
            field=models.PositiveSmallIntegerField(default=200, help_text='(On average, Americans eat 500 grams of chicken per week.)', verbose_name='Q3 - CHICKEN? (gram)'),
        ),
        migrations.AlterField(
            model_name='calculation',
            name='d4',
            field=models.PositiveSmallIntegerField(default=200, verbose_name='Q4 - FISH? (gram)'),
        ),
        migrations.AlterField(
            model_name='calculation',
            name='d5',
            field=models.PositiveSmallIntegerField(default=100, verbose_name='Q5 - CHEESE? (gram)'),
        ),
        migrations.AlterField(
            model_name='calculation',
            name='d6',
            field=models.PositiveSmallIntegerField(default=100, help_text='(e.g. milk, yogurt, ice-cream...)', verbose_name='Q6 - DAIRY? (gram)'),
        ),
        migrations.AlterField(
            model_name='calculation',
            name='d7',
            field=models.PositiveSmallIntegerField(default=14, verbose_name='Q7 - Eggs? (ea)'),
        ),
        migrations.AlterField(
            model_name='calculation',
            name='d8',
            field=models.PositiveSmallIntegerField(default=300, verbose_name='Q8 - Grains, vegetables, and fruit? (gram)'),
        ),
        migrations.AlterField(
            model_name='calculation',
            name='d9',
            field=models.PositiveSmallIntegerField(choices=[(0, 'None (0%)'), (25, 'Some (25%)'), (50, 'Half (50%)'), (75, 'Mostly (75%)'), (100, 'All (100%)')], default=75, help_text='(e.g. unprocessed or minimally processed food from wet market)', verbose_name='Q9 - How much of your food comes from within 500 km?'),
        ),
        migrations.AlterField(
            model_name='calculation',
            name='da',
            field=models.PositiveSmallIntegerField(choices=[(0, 'None (0%)'), (25, 'Some (25%)'), (50, 'Half (50%)'), (75, 'Mostly (75%)'), (100, 'All (100%)')], default=25, help_text='(e.g. processed food from Thailand or China)', verbose_name='Q10 - From 500-5000 km away?'),
        ),
        migrations.AlterField(
            model_name='calculation',
            name='db',
            field=models.PositiveSmallIntegerField(choices=[(0, 'None (0%)'), (25, 'Some (25%)'), (50, 'Half (50%)'), (75, 'Mostly (75%)'), (100, 'All (100%)')], default=0, help_text='(e.g. imported from Europe, Australia, US...)', verbose_name='Q11 - From more than 5000 km away?'),
        ),
        migrations.AlterField(
            model_name='calculation',
            name='e3',
            field=models.PositiveSmallIntegerField(default=1, help_text='(family or roommates living in the same space)', verbose_name='Q4 - How many people do you share your living space and your electricity bill with?'),
        ),
        migrations.AlterField(
            model_name='calculation',
            name='e4',
            field=models.PositiveSmallIntegerField(default=8, help_text='(e.g. office, coffee shop)', validators=[django.core.validators.MaxValueValidator(24), django.core.validators.MinValueValidator(0)], verbose_name='Q5 - How many hours per day do you spend in air-conditioning outside of your home?'),
        ),
        migrations.AlterField(
            model_name='calculation',
            name='e5',
            field=models.PositiveSmallIntegerField(default=1, help_text='(including yourself. E.g. crowded coffee shop with 20 people, or small office with 4 people)', validators=[django.core.validators.MinValueValidator(1)], verbose_name='Q6 - Roughly how many people share this in total?'),
        ),
        migrations.AlterField(
            model_name='calculation',
            name='f3',
            field=models.PositiveSmallIntegerField(default=50, validators=[django.core.validators.MinValueValidator(1)], verbose_name='Q4 - How big is your house, in m<sup>2</sup>?'),
        ),
        migrations.AlterField(
            model_name='calculation',
            name='offset',
            field=models.PositiveIntegerField(default=0, help_text='Offsets are measured in tonnes of carbon dioxide-equivalent (CO<sub>2</sub>e).', verbose_name='How much did you offset in the last 12 months?'),
        ),
    ]
