# Generated by Django 5.1.2 on 2024-10-08 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='clean_sheets',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='player',
            name='passes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='player',
            name='saves',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='player',
            name='tackles',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='player',
            name='first_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='player',
            name='last_name',
            field=models.CharField(max_length=100),
        ),
    ]
