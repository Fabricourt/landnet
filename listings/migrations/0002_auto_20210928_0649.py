# Generated by Django 3.1.3 on 2021-09-28 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='soil_type',
            field=models.CharField(choices=[('......', '......'), ('Cotton Soil', 'Cotton Soil'), ('Red Soil', 'Red Soil'), ('Sand Soil', 'Sand Soil'), ('Brown soil', 'Brown Soil')], default='......', max_length=100),
        ),
    ]
