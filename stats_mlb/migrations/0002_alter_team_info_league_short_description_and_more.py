# Generated by Django 5.0.3 on 2024-04-04 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stats_mlb', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team_info',
            name='League_Short_Description',
            field=models.CharField(max_length=3),
        ),
        migrations.AlterField(
            model_name='team_info',
            name='Sport_Short_Description',
            field=models.CharField(max_length=4),
        ),
    ]
