# Generated by Django 3.2.7 on 2021-10-05 09:48

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0024_alter_listing_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='description',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
