# Generated by Django 3.2.7 on 2021-10-01 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0007_alter_listing_sqft'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='sqft',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=10, null=True),
        ),
    ]