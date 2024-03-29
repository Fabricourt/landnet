# Generated by Django 3.2.7 on 2021-10-01 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0008_alter_listing_sqft'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='Large_plot_size',
            field=models.CharField(blank=True, help_text='only add plots larger than 10 acres', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='listing',
            name='plot_size',
            field=models.CharField(choices=[('......', '......'), ('40X80ft', '40X80ft'), ('50X100ft', '50X100ft'), ('100X100ft', '100X100ft'), ('1 Acre', '1 Acre'), ('2 Acre', '2 Acre'), ('3 Acre', '3 Acre'), ('4 Acre', '4 Acre'), ('5 Acre', '5 Acre'), ('6 Acre', '6 Acre'), ('7 Acre', '7 Acre'), ('8 Acre', '8 Acre'), ('9 Acre', '9 Acre'), ('10 Acre', '10 Acre')], default='......', max_length=100),
        ),
    ]
