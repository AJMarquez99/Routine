# Generated by Django 3.1.5 on 2021-02-11 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('routine', '0002_item'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='type',
            field=models.CharField(choices=[('FD', 'Food'), ('DV', 'Device'), ('HH', 'Household Object'), ('CL', 'Clothing'), ('MC', 'Misc')], max_length=30),
        ),
    ]
