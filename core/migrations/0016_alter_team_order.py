# Generated by Django 4.1.7 on 2023-03-23 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_team_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='order',
            field=models.IntegerField(),
        ),
    ]
