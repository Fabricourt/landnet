# Generated by Django 3.2.7 on 2021-10-02 06:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0015_auto_20211002_0937'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listing',
            name='listing_type',
        ),
    ]
