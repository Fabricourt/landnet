# Generated by Django 3.1.3 on 2021-10-04 03:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realtors', '0005_alter_realtor_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='realtor',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
