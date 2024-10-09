from django.db import models

class Player(models.Model):
    player_id = models.IntegerField(unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    team = models.CharField(max_length=100)
    position = models.CharField(max_length=20)
    goals = models.IntegerField(default=0) 
    assists = models.IntegerField(default=0)
    clean_sheets = models.IntegerField(default=0)
    saves = models.IntegerField(default=0)
    goals_conceded = models.IntegerField(default=0)
    minutes = models.IntegerField(default=0)
    penalties_saved = models.IntegerField(default=0)
    yellow_cards = models.IntegerField(default=0)
    red_cards = models.IntegerField(default=0)
    minutes_played = models.IntegerField(default=0)
    influence = models.FloatField(default=0.0)
    creativity = models.FloatField(default=0.0)
    threat = models.FloatField(default=0.0)
    expected_goals = models.FloatField(default=0.0)
    expected_assists = models.FloatField(default=0.0)
    expected_goal_involvements = models.FloatField(default=0.0)
    expected_goals_conceded = models.FloatField(default=0.0)
    total_points = models.IntegerField(default=0)
    

    def __str__(self):
        return f'{self.first_name} {self.last_name} ({self.position}) - {self.team}'

    class Meta:
        ordering = ['last_name', 'first_name']
