from django.db import models
from django import forms
from django.core.validators import MaxValueValidator, MinValueValidator
from django.core.exceptions import ValidationError


class Calculation(models.Model):
    name = models.CharField(
        max_length=30,
        default='Anonymous PP-er',
        blank=True,
    )
    email = models.EmailField(
        default='ppcfp@yopmail.com',
        blank=True,
    )
    offset = models.PositiveIntegerField(
        default=0,
        verbose_name="How much did you offset in the last 12 months?",
        help_text="Offsets are measured in tonnes of carbon dioxide-equivalent (CO<sub>2</sub>e).",
    )
    a1 = models.PositiveIntegerField(
        default=5000,
        verbose_name="Q1 - In the last 12 months, how far have you flown by plane? (km)",
        help_text="",
    )
    a2 = models.PositiveIntegerField(
        default=100,
        verbose_name="Q2 - by train? (km)",
        help_text="",
    )
    a3 = models.PositiveIntegerField(
        default=1000,
        verbose_name="Q3 - by bus? (km)",
        help_text="",
    )
    a4 = models.PositiveIntegerField(
        default=5000,
        verbose_name="Q4 - by car? (km)",
        help_text="",
    )
    a5 = models.PositiveIntegerField(
        default=5000,
        verbose_name="Q5 - by moto? (km)",
        help_text="",
    )
    b1 = models.PositiveSmallIntegerField(
        default=120,
        verbose_name="Q1 - In the last 12 months, how many NEW SMALL items have you purchased?",
        help_text="(e.g. socks, undies...)",
    )
    b2 = models.PositiveSmallIntegerField(
        default=48,
        verbose_name="Q2 - NEW MEDIUM-sized items?",
        help_text="(e.g. t-shirts, dresses...)",
    )
    b3 = models.PositiveSmallIntegerField(
        default=6,
        verbose_name="Q3 - NEW LARGE items?",
        help_text="(e.g. jeans, coats...)",
    )
    c1 = models.PositiveSmallIntegerField(
        default=10,
        verbose_name="Q1 - How many VERY SMALL appliances have you purchased in the last 12 months?",
        help_text="(e.g. earphones, computer mouse...)",
    )
    c2 = models.PositiveSmallIntegerField(
        default=1,
        validators=[MaxValueValidator(100), MinValueValidator(1)],
        verbose_name="Q2 - How many users do they have?",
        help_text="",
    )
    c3 = models.PositiveSmallIntegerField(
        default=10,
        verbose_name="Q3 - SMALL household appliances?",
        help_text="(e.g. kettle, toaster, iron, speakers...)",
    )
    c4 = models.PositiveSmallIntegerField(
        default=1,
        validators=[MaxValueValidator(100), MinValueValidator(1)],
        verbose_name="Q4 - How many users do they have?",
        help_text="",
    )
    c5 = models.PositiveSmallIntegerField(
        default=20,
        verbose_name="Q5 - MEDIUM-sized appliances?",
        help_text="(e.g. laptop, monitor, small fridge, desktop computer...)",
    )
    c6 = models.PositiveSmallIntegerField(
        default=1,
        validators=[MaxValueValidator(100), MinValueValidator(1)],
        verbose_name="Q6 - How many users do they have?",
        help_text="",
    )
    c7 = models.PositiveSmallIntegerField(
        default=10,
        verbose_name="Q7 - LARGE appliances?",
        help_text="(e.g. washing machine, large fridge...)",
    )
    c8 = models.PositiveSmallIntegerField(
        default=1,
        validators=[MaxValueValidator(100), MinValueValidator(1)],
        verbose_name="Q8 - How many users do they have?",
        help_text="",
    )
    d1 = models.PositiveSmallIntegerField(
        default=200,
        verbose_name="Q1 - How many grams of BEEF do you eat per week?",
        help_text="",
    )
    d2 = models.PositiveSmallIntegerField(
        default=200,
        verbose_name="Q2 - PORK? (gram)",
        help_text="",
    )
    d3 = models.PositiveSmallIntegerField(
        default=200,
        verbose_name="Q3 - CHICKEN? (gram)",
        help_text="(On average, Americans eat 500 grams of chicken per week.)",
    )
    d4 = models.PositiveSmallIntegerField(
        default=200,
        verbose_name="Q4 - FISH? (gram)",
        help_text="",
    )
    d5 = models.PositiveSmallIntegerField(
        default=100,
        verbose_name="Q5 - CHEESE? (gram)",
        help_text="",
    )
    d6 = models.PositiveSmallIntegerField(
        default=100,
        verbose_name="Q6 - DAIRY? (gram)",
        help_text="(e.g. milk, yogurt, ice-cream...)",
    )
    d7 = models.PositiveSmallIntegerField(
        default=14,
        verbose_name="Q7 - Eggs? (ea)",
        help_text="",
    )
    d8 = models.PositiveSmallIntegerField(
        default=300,
        verbose_name="Q8 - Grains, vegetables, and fruit? (gram)",
        help_text="",
    )

    class FoodFraction(models.IntegerChoices):
        NONE = 0, 'None (0%)'
        SOME = 25, 'Some (25%)'
        HALF = 50, 'Half (50%)'
        MOST = 75, 'Mostly (75%)'
        ALL = 100, 'All (100%)'

    d9 = models.PositiveSmallIntegerField(
        default=FoodFraction.MOST,
        verbose_name="Q9 - How much of your food comes from within 500 km?",
        help_text="(e.g. unprocessed or minimally processed food from wet market)",
        choices=FoodFraction.choices
    )
    da = models.PositiveSmallIntegerField(
        default=FoodFraction.SOME,
        verbose_name="Q10 - From 500-5000 km away?",
        help_text="(e.g. processed food from Thailand or China)",
        choices=FoodFraction.choices
    )
    db = models.PositiveSmallIntegerField(
        default=FoodFraction.NONE,
        verbose_name="Q11 - From more than 5000 km away?",
        help_text="(e.g. imported from Europe, Australia, US...)",
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
        verbose_name="Q4 - How many people do you share your living space and your electricity bill with?",
        help_text="(family or roommates living in the same space)",
    )
    e4 = models.PositiveSmallIntegerField(
        default=8,
        validators=[MaxValueValidator(24), MinValueValidator(0)],
        verbose_name="Q5 - How many hours per day do you spend in air-conditioning outside of your home?",
        help_text="(e.g. office, coffee shop...)",
    )
    e5 = models.PositiveSmallIntegerField(
        default=1,
        validators=[MinValueValidator(1)],
        verbose_name="Q6 - Roughly how many people share this in total?",
        help_text="(including yourself. E.g. crowded coffee shop with 20 people, or small office with 4 people)",
    )
    e6 = models.PositiveSmallIntegerField(
        default=800,
        validators=[MinValueValidator(500), MaxValueValidator(4000)],
        verbose_name="Q3 - What rate do you pay for electricity? (KHR/kWh)",
        help_text=""
    )
    f1 = models.PositiveSmallIntegerField(
        default=5,
        verbose_name="Q2 - How old is your house? (in years)",
        help_text="",
    )
    f2 = models.PositiveSmallIntegerField(
        default=20,
        validators=[MinValueValidator(1)],
        verbose_name="Q3 - How long do you think the house will be around? (in years)",
        help_text="",
    )
    f3 = models.PositiveSmallIntegerField(
        default=50,
        validators=[MinValueValidator(1)],
        verbose_name="Q4 - How big is your house?",
        help_text="(in m<sup>2</sup>)",
    )

    class HouseMaterial(models.IntegerChoices):
        CONCRETE = 1000, 'Bricks and concrete'
        WOOD = 0, "Wood"

    f4 = models.PositiveSmallIntegerField(
        default=HouseMaterial.CONCRETE,
        verbose_name="Q1 - What is your house primarily made of?",
        help_text="",
        choices=HouseMaterial.choices,
    )
    f5 = models.PositiveSmallIntegerField(
        default=4,
        validators=[MinValueValidator(1)],
        verbose_name="Q5 - How many people live in the house on average per year?",
        help_text="",
    )
    submit_time = models.DateTimeField(auto_now=True)
    cfp = models.FloatField(editable=False)
    planets = models.FloatField(editable=False)

    def clean(self):
        super().clean()
        if self.d9+self.da+self.db != 100:
            raise ValidationError({
                'd9': "Proportions don't add up to 100%.",
                'da': "Proportions don't add up to 100%.",
                'db': "Proportions don't add up to 100%.",
            })

    def save(self, *args, **kwargs):
        tranportation = (
            self.a1 * 0.18 +            # plane
            self.a2 * 0.06 +            # train
            self.a3 * 0.09 +            # bus
            self.a4 * 0.30 +            # car
            self.a5 * 0.26)            # moto
        clothes = (
            self.b1 * 4.72 +            # small items
            self.b2 * 11.80 +           # medium items
            self.b3 * 47.19)          # large items
        appliances = (
            self.c1 * 15 / self.c2 +    # very small appliances / their users
            self.c3 * 30 / self.c4 +    # small appliances / their users
            self.c5 * 300 / self.c6 +   # medium appliances / their users
            self.c7 * 1500 / self.c8)   # large appliances / their users
        food = (
            self.d1 * 0.027 * 52 +      # beef
            self.d2 * 0.012 * 52 +      # port
            self.d3 * 0.0069 * 52 +     # chicken
            self.d4 * 0.01 * 52 +       # fish
            self.d5 * 0.0135 * 52 +     # cheese
            self.d6 * 0.002 * 52 +      # dairy
            self.d7 * 0.2 * 52 +        # eggs
            self.d8 * 0.001 * 52 +      # grains and veg
            self.d9 * 9.3 / 100 +       # <500km
            self.da * 93 / 100 +        # <5000km
            self.db * 223.2 / 100)      # >= 5000km
        electricity = (
            self.e1 * 0.05 * (self.e2 * 4000/self.e6)/100 +
            self.e2 * (4000/self.e6) * 0.5 * ((100-self.e1)/100)*12 / self.e3 +
            self.e4 * self.e2 / self.e5)
        house = (self.f4 * self.f3 / (self.f1 + self.f2) / self.f5)
        self.cfp = (
            tranportation +
            clothes +
            appliances +
            food +
            electricity +
            house
        ) / 1000 - self.offset  # kg => ton, deduct offset
        self.planets = self.cfp / 3
        super(Calculation, self).save(*args, **kwargs)

    class Meta:
        ordering = [
            'name', 'email', 'offset',
            'a1', 'a2', 'a3', 'a4', 'a5',
            'b1', 'b2', 'b3',
            'c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c8',
            'd1', 'd2', 'd3', 'd4', 'd5', 'd6', 'd7', 'd8', 'd9', 'da', 'db',
            'e1', 'e2', 'e3', 'e4', 'e5', 'e6',
            'f4', 'f1', 'f2', 'f3', 'f5',
            'cfp', 'planets'
        ]
