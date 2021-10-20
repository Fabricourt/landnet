# Generated by Django 3.2.7 on 2021-10-02 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realtors', '0003_alter_realtor_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='realtor',
            old_name='phone',
            new_name='mobile',
        ),
        migrations.AddField(
            model_name='realtor',
            name='fax',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='realtor',
            name='office',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='realtor',
            name='whatsapp',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
