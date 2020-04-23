# Generated by Django 3.0.5 on 2020-04-23 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ppco2', '0007_auto_20200422_2331'),
    ]

    operations = [
        migrations.AddField(
            model_name='calculation',
            name='offset',
            field=models.PositiveIntegerField(default=0, help_text='Offsets are measured in tonnes of carbon dioxide-equivalent (CO<sup>2</sup>e).', verbose_name='How much did you offset in the last 12 months?'),
        ),
    ]
