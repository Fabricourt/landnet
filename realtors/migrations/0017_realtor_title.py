# Generated by Django 3.2.8 on 2021-10-28 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realtors', '0016_alter_realtor_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='realtor',
            name='title',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
