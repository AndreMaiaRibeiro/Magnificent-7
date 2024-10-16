# Generated by Django 5.1.2 on 2024-10-08 22:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0008_remove_player_passes_remove_player_tackles_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='expected_assists',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='player',
            name='expected_goal_involvements',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='player',
            name='expected_goals',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='player',
            name='expected_goals_conceded',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='player',
            name='minutes',
            field=models.IntegerField(default=0),
        ),
    ]
