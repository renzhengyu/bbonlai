# Generated by Django 3.0.5 on 2020-05-01 17:52

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Calculation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='Anonymous PP-er', max_length=30)),
                ('email', models.EmailField(blank=True, default='ppcfp@yopmail.com', max_length=254)),
                ('offset', models.PositiveIntegerField(default=0, help_text='Offsets are measured in tonnes of carbon dioxide-equivalent (CO<sub>2</sub>e).', verbose_name='How much did you offset in the last 12 months?')),
                ('a1', models.PositiveIntegerField(default=5000, verbose_name='Q1 - In the last 12 months, how far have you flown by plane? (km)')),
                ('a2', models.PositiveIntegerField(default=100, verbose_name='Q2 - by train? (km)')),
                ('a3', models.PositiveIntegerField(default=1000, verbose_name='Q3 - by bus? (km)')),
                ('a4', models.PositiveIntegerField(default=5000, verbose_name='Q4 - by car? (km)')),
                ('a5', models.PositiveIntegerField(default=5000, verbose_name='Q5 - by moto? (km)')),
                ('b1', models.PositiveSmallIntegerField(default=120, help_text='(e.g. socks, undies...)', verbose_name='Q1 - In the last 12 months, how many NEW SMALL items have you purchased?')),
                ('b2', models.PositiveSmallIntegerField(default=48, help_text='(e.g. t-shirts, dresses...)', verbose_name='Q2 - NEW MEDIUM-sized items?')),
                ('b3', models.PositiveSmallIntegerField(default=6, help_text='(e.g. jeans, coats...)', verbose_name='Q3 - NEW LARGE items?')),
                ('c1', models.PositiveSmallIntegerField(default=10, help_text='(e.g. earphones, computer mouse...)', verbose_name='Q1 - How many VERY SMALL appliances have you purchased in the last 12 months?')),
                ('c2', models.PositiveSmallIntegerField(default=1, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(1)], verbose_name='Q2 - How many users do they have?')),
                ('c3', models.PositiveSmallIntegerField(default=10, help_text='(e.g. kettle, toaster, iron, speakers...)', verbose_name='Q3 - SMALL household appliances?')),
                ('c4', models.PositiveSmallIntegerField(default=1, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(1)], verbose_name='Q4 - How many users do they have?')),
                ('c5', models.PositiveSmallIntegerField(default=20, help_text='(e.g. laptop, monitor, small fridge, desktop computer...)', verbose_name='Q5 - MEDIUM-sized appliances?')),
                ('c6', models.PositiveSmallIntegerField(default=1, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(1)], verbose_name='Q6 - How many users do they have?')),
                ('c7', models.PositiveSmallIntegerField(default=10, help_text='(e.g. washing machine, large fridge...)', verbose_name='Q7 - LARGE appliances?')),
                ('c8', models.PositiveSmallIntegerField(default=1, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(1)], verbose_name='Q8 - How many users do they have?')),
                ('d1', models.PositiveSmallIntegerField(default=200, verbose_name='Q1 - How many grams of BEEF do you eat per week?')),
                ('d2', models.PositiveSmallIntegerField(default=200, verbose_name='Q2 - PORK? (gram)')),
                ('d3', models.PositiveSmallIntegerField(default=200, help_text='(On average, Americans eat 500 grams of chicken per week.)', verbose_name='Q3 - CHICKEN? (gram)')),
                ('d4', models.PositiveSmallIntegerField(default=200, verbose_name='Q4 - FISH? (gram)')),
                ('d5', models.PositiveSmallIntegerField(default=100, verbose_name='Q5 - CHEESE? (gram)')),
                ('d6', models.PositiveSmallIntegerField(default=100, help_text='(e.g. milk, yogurt, ice-cream...)', verbose_name='Q6 - DAIRY? (gram)')),
                ('d7', models.PositiveSmallIntegerField(default=14, verbose_name='Q7 - Eggs? (ea)')),
                ('d8', models.PositiveSmallIntegerField(default=300, verbose_name='Q8 - Grains, vegetables, and fruit? (gram)')),
                ('d9', models.PositiveSmallIntegerField(choices=[(0, 'None (0%)'), (25, 'Some (25%)'), (50, 'Half (50%)'), (75, 'Mostly (75%)'), (100, 'All (100%)')], default=75, help_text='(e.g. unprocessed or minimally processed food from wet market)', verbose_name='Q9 - How much of your food comes from within 500 km?')),
                ('da', models.PositiveSmallIntegerField(choices=[(0, 'None (0%)'), (25, 'Some (25%)'), (50, 'Half (50%)'), (75, 'Mostly (75%)'), (100, 'All (100%)')], default=25, help_text='(e.g. processed food from Thailand or China)', verbose_name='Q10 - From 500-5000 km away?')),
                ('db', models.PositiveSmallIntegerField(choices=[(0, 'None (0%)'), (25, 'Some (25%)'), (50, 'Half (50%)'), (75, 'Mostly (75%)'), (100, 'All (100%)')], default=0, help_text='(e.g. imported from Europe, Australia, US...)', verbose_name='Q11 - From more than 5000 km away?')),
                ('e1', models.PositiveSmallIntegerField(choices=[(0, 'None (0%)'), (25, 'Some (25%)'), (50, 'Half (50%)'), (75, 'Mostly (75%)'), (100, 'All (100%)')], default=0, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)], verbose_name='Q1 - How much of your electricity needs are covered by your solar panels?')),
                ('e2', models.FloatField(default=50, verbose_name='Q2 - How much is your monthly electricity bill? (USD)')),
                ('e3', models.PositiveSmallIntegerField(default=1, help_text='(family or roommates living in the same space)', verbose_name='Q4 - How many people do you share your living space and your electricity bill with?')),
                ('e4', models.PositiveSmallIntegerField(default=8, help_text='(e.g. office, coffee shop...)', validators=[django.core.validators.MaxValueValidator(24), django.core.validators.MinValueValidator(0)], verbose_name='Q5 - How many hours per day do you spend in air-conditioning outside of your home?')),
                ('e5', models.PositiveSmallIntegerField(default=1, help_text='(including yourself. E.g. crowded coffee shop with 20 people, or small office with 4 people)', validators=[django.core.validators.MinValueValidator(1)], verbose_name='Q6 - Roughly how many people share this in total?')),
                ('e6', models.PositiveSmallIntegerField(default=800, validators=[django.core.validators.MinValueValidator(500), django.core.validators.MaxValueValidator(4000)], verbose_name='Q3 - What rate do you pay for electricity? (KHR/kWh)')),
                ('f1', models.PositiveSmallIntegerField(default=5, verbose_name='Q2 - How old is your house? (in years)')),
                ('f2', models.PositiveSmallIntegerField(default=20, verbose_name='Q3 - How long do you think the house will be around? (in years)')),
                ('f3', models.PositiveSmallIntegerField(default=50, help_text='(in m<sup>2</sup>)', validators=[django.core.validators.MinValueValidator(1)], verbose_name='Q4 - How big is your house?')),
                ('f4', models.PositiveSmallIntegerField(choices=[(1000, 'Bricks and concrete'), (0, 'Wood')], default=1000, verbose_name='Q1 - What is your house primarily made of?')),
                ('f5', models.PositiveSmallIntegerField(default=4, validators=[django.core.validators.MinValueValidator(1)], verbose_name='Q5 - How many people live in the house on average per year?')),
                ('submit_time', models.DateTimeField(auto_now=True)),
                ('cfp', models.FloatField(editable=False)),
                ('planets', models.FloatField(editable=False)),
            ],
            options={
                'ordering': ['name', 'email', 'offset', 'a1', 'a2', 'a3', 'a4', 'a5', 'b1', 'b2', 'b3', 'c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c8', 'd1', 'd2', 'd3', 'd4', 'd5', 'd6', 'd7', 'd8', 'd9', 'da', 'db', 'e1', 'e2', 'e3', 'e4', 'e5', 'e6', 'f4', 'f1', 'f2', 'f3', 'f5', 'cfp', 'planets'],
            },
        ),
    ]
