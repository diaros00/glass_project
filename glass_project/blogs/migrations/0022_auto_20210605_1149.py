# Generated by Django 3.1 on 2021-06-05 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0021_delete_modelglasswithdefect_for_export'),
    ]

    operations = [
        migrations.AlterField(
            model_name='defect',
            name='defect_name',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='modelglass',
            name='model_code',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='modelglass',
            name='model_name',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='modelglasswithdefect',
            name='model_code',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='modelglasswithdefect',
            name='model_name',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='modelglasswithdefect',
            name='shift',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='department',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='shift',
            field=models.TextField(),
        ),
    ]
