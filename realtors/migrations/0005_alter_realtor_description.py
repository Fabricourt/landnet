# Generated by Django 3.2.7 on 2021-10-02 20:23

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('realtors', '0004_auto_20211002_2203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='realtor',
            name='description',
            field=ckeditor.fields.RichTextField(blank=True),
        ),
    ]