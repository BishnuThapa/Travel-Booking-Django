# Generated by Django 4.1.7 on 2023-03-27 04:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0022_alter_inquiry_email_alter_inquiry_message_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='inquiry',
            options={'verbose_name': 'Inquiry', 'verbose_name_plural': "Customer's Inquiry"},
        ),
        migrations.AddField(
            model_name='inquiry',
            name='phone',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
