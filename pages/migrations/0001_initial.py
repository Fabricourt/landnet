# Generated by Django 3.2.7 on 2021-10-24 09:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Pages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='particular name of the area as known to the locals', max_length=50, null=True, unique=True)),
                ('slug', models.SlugField(max_length=250, unique_for_date='publish')),
                ('description', models.TextField(blank=True, null=True)),
                ('photo', models.ImageField(blank=True, help_text='your image must be jpg format to save', null=True, upload_to='Pages_photos/%Y/%m/%d/')),
                ('youtube', models.TextField(blank=True, null=True)),
                ('video', models.FileField(blank=True, null=True, upload_to='videos/')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('mvp', models.BooleanField(default=False)),
                ('about', models.BooleanField(default=False)),
                ('service', models.BooleanField(default=False)),
                ('policy', models.BooleanField(default=False)),
                ('privacy', models.BooleanField(default=False)),
                ('cookies', models.BooleanField(default=False)),
                ('published', models.BooleanField(default=True)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('title',),
            },
        ),
    ]