# Generated by Django 3.1 on 2021-06-05 07:07

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blogs', '0027_auto_20210605_1404'),
    ]

    operations = [
        migrations.CreateModel(
            name='modelGlass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_code', models.CharField(max_length=200, null=True)),
                ('model_name', models.CharField(max_length=200, null=True)),
                ('model_desc', models.CharField(max_length=200, null=True)),
                ('model_image', models.ImageField(null=True, upload_to='image/', verbose_name='')),
            ],
        ),
        migrations.CreateModel(
            name='modelGlassWithDefect',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_create', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('model_code', models.CharField(max_length=200, null=True)),
                ('model_name', models.CharField(max_length=200, null=True)),
                ('model_desc', models.CharField(max_length=200, null=True)),
                ('defect_name1', models.CharField(max_length=200, null=True)),
                ('defect_name2', models.CharField(max_length=200, null=True)),
                ('defect_name3', models.CharField(max_length=200, null=True)),
                ('defect_name4', models.CharField(max_length=200, null=True)),
                ('defect_name5', models.CharField(max_length=200, null=True)),
                ('department', models.CharField(max_length=200, null=True)),
                ('point_defect', models.CharField(max_length=200, null=True)),
                ('date_select', models.DateField()),
                ('shift', models.CharField(max_length=200, null=True)),
                ('number_glass', models.CharField(max_length=200, null=True)),
                ('status_glass', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.CharField(max_length=200, null=True)),
                ('shift', models.CharField(max_length=30, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
