# Generated by Django 3.1 on 2021-05-17 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0009_auto_20210515_1135'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='modelglasswithdefect',
            name='defect_name',
        ),
        migrations.AddField(
            model_name='modelglasswithdefect',
            name='defect_name1',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='modelglasswithdefect',
            name='defect_name2',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='modelglasswithdefect',
            name='defect_name3',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='modelglasswithdefect',
            name='defect_name4',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='modelglasswithdefect',
            name='defect_name5',
            field=models.CharField(max_length=200, null=True),
        ),
    ]