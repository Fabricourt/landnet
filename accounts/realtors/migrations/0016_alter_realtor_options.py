# Generated by Django 3.2.8 on 2021-10-28 10:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('realtors', '0015_realtor_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='realtor',
            options={'ordering': ('-hire_date',), 'verbose_name': 'Team member', 'verbose_name_plural': 'Team members'},
        ),
    ]
