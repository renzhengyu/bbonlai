from django.db import models
from django import forms
from django.core.validators import MaxValueValidator, MinValueValidator
from django.core.exceptions import ValidationError


class Calculation(models.Model):
    submit_time = models.DateTimeField(auto_now=True)
    cfp = models.FloatField()
    planets = models.FloatField()
    name = models.CharField(
        max_length=30,
        default='Anonymous PP-er',
        blank=True,
    )
    email = models.EmailField(
        default='ppcfp@yopmail.com',
        blank=True,
    )
    a1 = models.PositiveIntegerField(
        default=5000,
        verbose_name="Q1 - How far have you flown by plane in the last 12 months? (km)",
        help_text="",
    )
    a2 = models.PositiveIntegerField(
        default=100,
        verbose_name="Q2 - How far have you taken trains in the last 12 months? (km)",
        help_text="",
    )
    a3 = models.PositiveIntegerField(
        default=1000,
        verbose_name="Q3 - How far have you taken buses in the last 12 months? (km)",
        help_text="",
    )
    a4 = models.PositiveIntegerField(
        default=5000,
        verbose_name="Q4 - How far have you taken cars in the last 12 months? (km)",
        help_text="",
    )
    a5 = models.PositiveIntegerField(
        default=5000,
        verbose_name="Q5 - How far have you taken motos in the last 12 months? (km)",
        help_text="",
    )
    b1 = models.PositiveSmallIntegerField(
        default=120,
        verbose_name="Q1 - How many small items (socks, undies) have you purchased in the last 12 months?",
        help_text="",
    )
    b2 = models.PositiveSmallIntegerField(
        default=48,
        verbose_name="Q2 - How many medium size items (t-shirts, dresses) have you purchased in the last 12 months?",
        help_text="",
    )
    b3 = models.PositiveSmallIntegerField(
        default=6,
        verbose_name="Q3 - How many large items (jeans, coats)?",
        help_text="",
    )
    c1 = models.PositiveSmallIntegerField(
        default=10,
        verbose_name="Q1 - How many very small appliance (earphones, computer mouse..) have you purchased in the last 12 months?",
        help_text="",
    )
    c2 = models.PositiveSmallIntegerField(
        default=1,
        validators=[MaxValueValidator(100), MinValueValidator(1)],
        verbose_name="Q2 - How many users do they have?",
        help_text="",
    )
    c3 = models.PositiveSmallIntegerField(
        default=10,
        verbose_name="Q3 - How many small household appliance (kettle, toaster, iron, speakers...) have you purchased in the last 12 months?",
        help_text="",
    )
    c4 = models.PositiveSmallIntegerField(
        default=1,
        validators=[MaxValueValidator(100), MinValueValidator(1)],
        verbose_name="Q4 - How many users do they have?",
        help_text="",
    )
    c5 = models.PositiveSmallIntegerField(
        default=20,
        verbose_name="Q5 - How many medium-sized appliances (laptop, monitor, small fridge, desktop computer) have you purchased in the last 12 months?",
        help_text="",
    )
    c6 = models.PositiveSmallIntegerField(
        default=1,
        validators=[MaxValueValidator(100), MinValueValidator(1)],
        verbose_name="Q6 - How many users do they have?",
        help_text="",
    )
    c7 = models.PositiveSmallIntegerField(
        default=10,
        verbose_name="Q7 - Large appliances (washing machine, large fridge..)",
        help_text="",
    )
    c8 = models.PositiveSmallIntegerField(
        default=1,
        validators=[MaxValueValidator(100), MinValueValidator(1)],
        verbose_name="Q8 - How many users do they have?",
        help_text="",
    )
    d1 = models.PositiveSmallIntegerField(
        default=200,
        verbose_name="Q1 - How many grams of beef do you eat per week?",
        help_text="",
    )
    d2 = models.PositiveSmallIntegerField(
        default=200,
        verbose_name="Q2 - How many grams of pork do you eat per week?",
        help_text="",
    )
    d3 = models.PositiveSmallIntegerField(
        default=200,
        verbose_name="Q3 - How many grams of chicken do you eat per week?",
        help_text="",
    )
    d4 = models.PositiveSmallIntegerField(
        default=200,
        verbose_name="Q4 - How many grams of fish do you eat per week?",
        help_text="",
    )
    d5 = models.PositiveSmallIntegerField(
        default=100,
        verbose_name="Q5 - How many grams of cheese do you eat per week?",
        help_text="",
    )
    d6 = models.PositiveSmallIntegerField(
        default=100,
        verbose_name="Q6 - How many grams of milk, yogurt, ice-cream, do you eat per week?",
        help_text="",
    )
    d7 = models.PositiveSmallIntegerField(
        default=14,
        verbose_name="Q7 - How many eggs do you eat per week?",
        help_text="",
    )
    d8 = models.PositiveSmallIntegerField(
        default=300,
        verbose_name="Q8 - How many grams of grains, vegetables, and fruit do you eat per week?",
        help_text="",
    )

    class FoodFraction(models.IntegerChoices):
        NONE = 0, 'None'
        SOME = 25, 'Some'
        HALF = 50, 'Half'
        MOST = 75, 'Mostly'
        ALL = 100, 'All'

    d9 = models.PositiveSmallIntegerField(
        default=FoodFraction.MOST,
        verbose_name="Q9 - How much of your food comes from within 500 km (e.g. unprocessed or minimally processed food from wet market)?",
        help_text="",
        choices=FoodFraction.choices
    )
    da = models.PositiveSmallIntegerField(
        default=FoodFraction.SOME,
        verbose_name="Q10 - How much of your food comes from 500-5000 km away (e.g. processed food from Thailand or China)?",
        help_text="",
        choices=FoodFraction.choices
    )
    db = models.PositiveSmallIntegerField(
        default=FoodFraction.NONE,
        verbose_name="Q11 - How much of your food comes from more than 5000 km away (imported from Europe, Australia, US..)",
        help_text="",
        choices=FoodFraction.choices
    )
    e1 = models.PositiveSmallIntegerField(
        default=FoodFraction.NONE,
        validators=[MaxValueValidator(100), MinValueValidator(0)],
        verbose_name="Q1 - How much of your electricity needs are covered by your solar panels?",
        help_text="",
        choices=FoodFraction.choices
    )
    e2 = models.FloatField(
        default=50,
        verbose_name="Q2 - How much is your monthly electricity bill? (USD)",
        help_text="",
    )
    e3 = models.PositiveSmallIntegerField(
        default=1,
        verbose_name="Q3 - How many people do you share your living space and your electricity bill with (family or roommates living in the same space)?",
        help_text="",
    )
    e4 = models.PositiveSmallIntegerField(
        default=8,
        validators=[MaxValueValidator(24), MinValueValidator(0)],
        verbose_name="Q4 - How many hours per day do you spend in air-conditioning outside of your home (e.g. office, coffee shop)",
        help_text="",
    )
    e5 = models.PositiveSmallIntegerField(
        default=1,
        validators=[MinValueValidator(1)],
        verbose_name="Q5 - Roughly how many people share this in total (including yourself. E.g. crowded coffee shop with 20 people, or small office with 4 people)?",
        help_text="",
    )
    f1 = models.PositiveSmallIntegerField(
        default=5,
        verbose_name="Q1 - How old is your house? (in years)",
        help_text="",
    )
    f2 = models.PositiveSmallIntegerField(
        default=20,
        verbose_name="Q2 - How long do you think the house will be around? (in years)",
        help_text="",
    )
    f3 = models.PositiveSmallIntegerField(
        default=50,
        validators=[MinValueValidator(1)],
        verbose_name="Q3 - How big is your house, in square meters?",
        help_text="",
    )

    class HouseMaterial(models.IntegerChoices):
        CONCRETE = 100, 'Bricks and concrete'
        WOOD = 10, "Wood"

    f4 = models.PositiveSmallIntegerField(
        default=HouseMaterial.CONCRETE,
        verbose_name="Q4 - What is your house primarily made of?",
        help_text="",
        choices=HouseMaterial.choices,
    )
    f5 = models.PositiveSmallIntegerField(
        default=4,
        validators=[MinValueValidator(1)],
        verbose_name="Q5 - How many people live in the house on average per year?",
        help_text="",
    )

    def clean(self):
        if self.d9+self.da+self.db != 100:
            raise ValidationError({
                'd9':"Proportions don't add up to 100%.",
                'da':"Proportions don't add up to 100%.",
                'db':"Proportions don't add up to 100%.",
                })
