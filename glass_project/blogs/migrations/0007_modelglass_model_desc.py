# Generated by Django 3.1 on 2021-05-11 02:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0006_auto_20210511_0952'),
    ]

    operations = [
        migrations.AddField(
            model_name='modelglass',
            name='model_desc',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
