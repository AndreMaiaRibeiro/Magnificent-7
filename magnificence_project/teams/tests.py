from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Player
from .score_calculator import *

class MagnificentSevenAPITests(TestCase):
    def setUp(self):
        self.client = APIClient()

        # Create some test players with explicit player_id and new fields
        Player.objects.create(
            player_id=1, first_name="Ederson", last_name="Moraes", position="Goalkeeper", team="Man Utd", 
            saves=10, clean_sheets=5, goals_conceded=2, penalties_saved=1, expected_goals_conceded=2.5, minutes_played=500, total_points=27
        )
        Player.objects.create(
            player_id=2, first_name="Ruben", last_name="Dias", position="Defender", team="Man Utd", 
            goals=2, assists=2, clean_sheets=4, goals_conceded=3, expected_goals_conceded=1.5, minutes_played=600, total_points=34
        )
        Player.objects.create(
            player_id=3, first_name="John", last_name="Stones", position="Defender", team="Man Utd", 
            goals=1, assists=1, clean_sheets=3, goals_conceded=4, expected_goals_conceded=2.0, minutes_played=550, total_points=19
        )
        Player.objects.create(
            player_id=4, first_name="Kevin", last_name="De Bruyne", position="Midfielder", team="Man Utd", 
            goals=5, assists=6, creativity=150, influence=300, expected_goal_involvements=5.5, expected_assists=3.0, minutes_played=800, total_points=67
        )
        Player.objects.create(
            player_id=5, first_name="Bernardo", last_name="Silva", position="Midfielder", team="Man Utd", 
            goals=3, assists=3, creativity=120, influence=250, expected_goal_involvements=4.0, expected_assists=2.0, minutes_played=700, total_points=53
        )
        Player.objects.create(
            player_id=6, first_name="Phil", last_name="Foden", position="Midfielder", team="Man Utd", 
            goals=4, assists=2, creativity=100, influence=180, expected_goal_involvements=3.0, expected_assists=1.5, minutes_played=500, total_points=38
        )
        Player.objects.create(
            player_id=7, first_name="Erling", last_name="Haaland", position="Forward", team="Man Utd", 
            goals=12, assists=3, threat=250, influence=350, expected_goal_involvements=10.5, expected_goals=8.0, expected_assists=2.5, minutes_played=850, total_points=76
        )

    def test_get_magnificent_seven(self):
        # Test the all-time best players endpoint
        url = reverse('magnificent_seven')
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 7)

        # Ensure the positions are correctly returned in the response
        self.assertEqual(response.data[0]['position'], 'Goalkeeper')
        self.assertEqual(response.data[1]['position'], 'Defender')
        self.assertEqual(response.data[2]['position'], 'Defender')
        self.assertEqual(response.data[3]['position'], 'Midfielder')
        self.assertEqual(response.data[4]['position'], 'Midfielder')
        self.assertEqual(response.data[5]['position'], 'Midfielder')
        self.assertEqual(response.data[6]['position'], 'Forward')

        # Ensure all required fields are present in the response
        for player in response.data:
            self.assertIn('name', player)
            self.assertIn('position', player)
            self.assertIn('team', player)
            self.assertIn('goals', player)
            self.assertIn('assists', player)
            self.assertIn('clean_sheets', player)
            self.assertIn('saves', player)
            self.assertIn('expected_goals_conceded', player)
            self.assertIn('expected_goal_involvements', player)
            self.assertIn('creativity', player)
            self.assertIn('influence', player)
            self.assertIn('minutes_played', player)
            self.assertIn('total_points', player)
            self.assertIn('performance_score', player)

    def test_get_magnificent_seven_for_team(self):
        # Test the team-based magnificent seven endpoint
        url = reverse('magnificent_seven_team', kwargs={'team_name': 'Man Utd'})
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 7)

        # Check all returned players belong to the correct team
        for player in response.data:
            self.assertEqual(player['team'], 'Man Utd')

        # Ensure all required fields are present in the response
        for player in response.data:
            self.assertIn('name', player)
            self.assertIn('position', player)
            self.assertIn('team', player)
            self.assertIn('goals', player)
            self.assertIn('assists', player)
            self.assertIn('clean_sheets', player)
            self.assertIn('saves', player)
            self.assertIn('expected_goals_conceded', player)
            self.assertIn('expected_goal_involvements', player)
            self.assertIn('creativity', player)
            self.assertIn('influence', player)
            self.assertIn('minutes_played', player)
            self.assertIn('total_points', player)
            self.assertIn('performance_score', player)
