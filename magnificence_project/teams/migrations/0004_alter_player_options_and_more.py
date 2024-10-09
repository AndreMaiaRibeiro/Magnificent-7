# Generated by Django 5.1.2 on 2024-10-08 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0003_player_penalties_saved_alter_player_first_name_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='player',
            options={'ordering': ['last_name', 'first_name']},
        ),
        migrations.RenameField(
            model_name='player',
            old_name='magnificence',
            new_name='minutes_played',
        ),
        migrations.RenameField(
            model_name='player',
            old_name='passes',
            new_name='red_cards',
        ),
        migrations.RenameField(
            model_name='player',
            old_name='tackles',
            new_name='yellow_cards',
        ),
        migrations.RemoveField(
            model_name='player',
            name='player_id',
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
        migrations.AlterField(
            model_name='player',
            name='position',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='player',
            name='team',
            field=models.CharField(max_length=100),
        ),
    ]
