# Generated by Django 3.2.7 on 2021-10-02 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0014_auto_20211001_2222'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='listing_type',
            field=models.CharField(blank=True, choices=[('Rental', 'Rental'), ('House', 'House'), ('Plot', 'Plot')], max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='listing',
            name='mvp',
            field=models.BooleanField(default=False),
        ),
    ]