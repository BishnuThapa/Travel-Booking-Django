# Generated by Django 4.1.7 on 2023-03-22 09:42

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_aboutus'),
    ]

    operations = [
        migrations.CreateModel(
            name='WhyUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.ImageField(upload_to='whyus')),
                ('heading', models.CharField(max_length=255)),
                ('description', ckeditor.fields.RichTextField()),
            ],
            options={
                'verbose_name': 'Why Us',
                'verbose_name_plural': 'Why Us',
            },
        ),
    ]