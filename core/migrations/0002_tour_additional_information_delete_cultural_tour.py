# Generated by Django 4.1.7 on 2023-03-21 09:57

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tour',
            name='additional_information',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.DeleteModel(
            name='Cultural_Tour',
        ),
    ]
