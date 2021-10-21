# Generated by Django 3.2.7 on 2021-09-20 19:39

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('realtors', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('neighbourhood', models.CharField(max_length=200)),
                ('town', models.CharField(max_length=100)),
                ('county', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
                ('price', models.IntegerField()),
                ('plot_type', models.CharField(choices=[('......', '......'), ('Beach', 'Beach'), ('Residential', 'Residential'), ('Commercial', 'Commercial'), ('Farm', 'Farm'), ('Ranch', 'Ranch')], default='......', max_length=100)),
                ('soil_type', models.CharField(choices=[('......', '......'), ('Cotton', 'Cotton'), ('Red', 'Red'), ('Sand', 'Sand'), ('Ranch', 'Ranch')], default='......', max_length=100)),
                ('plot_size', models.CharField(choices=[('......', '......'), ('40X80ft', '40X80ft'), ('50X100ft', '50X100ft'), ('100X100ft', '100X100ft'), ('1 Acre', '1 Acre'), ('2 Acre', '2 Acre'), ('3 Acre', '3 Acre'), ('4 Acre', '4 Acre'), ('5 Acre', '5 Acre'), ('6 Acre', '6 Acre'), ('7 Acre', '7 Acre'), ('8 Acre', '8 Acre'), ('9 Acre', '9 Acre'), ('10 Acre', '10 Acre'), ('100+ Acre', '100+ Acre')], default='......', max_length=100)),
                ('photo_main', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('photo_1', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('photo_2', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('photo_3', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('photo_4', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('photo_5', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('photo_6', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('sold', models.BooleanField(default=False)),
                ('is_published', models.BooleanField(default=True)),
                ('list_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('realtor', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='realtors.realtor')),
            ],
        ),
    ]