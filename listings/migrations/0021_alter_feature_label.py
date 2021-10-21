# Generated by Django 3.2.7 on 2021-10-02 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0020_listing_features'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feature',
            name='label',
            field=models.CharField(help_text='property features', max_length=200, unique=True),
        ),
    ]