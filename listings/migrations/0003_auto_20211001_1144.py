# Generated by Django 3.2.7 on 2021-10-01 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0002_auto_20210928_0649'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='House',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='listing',
            name='Rental',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='listing',
            name='bathrooms',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=2, null=True),
        ),
        migrations.AddField(
            model_name='listing',
            name='bedrooms',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='listing',
            name='garage',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='listing',
            name='house_type',
            field=models.CharField(choices=[('......', '......'), ('Mansionnete', 'Mansionnete'), ('Bungalow', 'Bungalow'), ('Apartment', 'Apartment'), ('Studio', 'Studio'), ('Alcove Studio', 'Alcove Studio'), ('Convertible Studio', 'Convertible Studio'), ('Convertible Studio', 'Convertible Studio'), ('Duplex/Triplex', 'Duplex/Triplex'), ('Junior 1 Bedroom', 'Junior 1 Bedroom'), ('Garden Apartment', 'Garden Apartment'), ('Railroad Apartment', 'Railroad Apartment')], default='......', max_length=100),
        ),
        migrations.AddField(
            model_name='listing',
            name='lot_size',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=5, null=True),
        ),
        migrations.AddField(
            model_name='listing',
            name='plot',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='listing',
            name='sqft',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='listing',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
