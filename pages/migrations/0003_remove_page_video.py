# Generated by Django 3.2.7 on 2021-10-24 10:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_rename_pages_page'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='page',
            name='video',
        ),
    ]