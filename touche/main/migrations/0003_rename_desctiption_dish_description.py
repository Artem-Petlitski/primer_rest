# Generated by Django 4.0 on 2022-01-14 19:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_contact_alter_dish_options'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dish',
            old_name='desctiption',
            new_name='description',
        ),
    ]