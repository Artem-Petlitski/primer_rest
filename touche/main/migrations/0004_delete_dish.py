# Generated by Django 4.0 on 2022-01-14 19:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_rename_desctiption_dish_description'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Dish',
        ),
    ]