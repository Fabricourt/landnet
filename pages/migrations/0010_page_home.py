# Generated by Django 3.2.8 on 2021-10-28 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0009_alter_page_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='home',
            field=models.BooleanField(default=False),
        ),
    ]
