# Generated by Django 3.2.7 on 2021-10-01 15:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0005_alter_listing_bathrooms'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listing',
            name='lot_size',
        ),
    ]