# Generated by Django 3.2.8 on 2021-10-28 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_alter_page_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='Faq',
            field=models.BooleanField(default=False),
        ),
    ]
