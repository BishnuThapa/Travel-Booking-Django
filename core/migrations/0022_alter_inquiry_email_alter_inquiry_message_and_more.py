# Generated by Django 4.1.7 on 2023-03-27 04:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0021_rename_contactmessages_inquiry'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inquiry',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='inquiry',
            name='message',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='inquiry',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='inquiry',
            name='subject',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
