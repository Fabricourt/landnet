# Generated by Django 3.1.3 on 2021-10-04 04:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('realtors', '0008_realtor_bio'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='realtor',
            name='description',
        ),
    ]
