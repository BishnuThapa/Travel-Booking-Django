# Generated by Django 4.1.7 on 2023-03-27 07:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0028_flightbooking'),
    ]

    operations = [
        migrations.RenameField(
            model_name='flightbooking',
            old_name='contact',
            new_name='phone',
        ),
    ]
