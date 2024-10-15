from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.cache import cache
from .models import Player
from .services import fetch_and_save_players
from django.db.models.functions import Lower
from .score_calculator import *
from .select_best import *

class ApiHomeView(APIView):
    def get(self, request):
        fetch_and_save_players()
        return render(request, 'api_home.html')


class TeamsListView(APIView):
    def get(self, request):
        # Fetch distinct team names, ensuring case-insensitivity and removing whitespace
        teams = Player.objects.annotate(cleaned_team=Lower('team')).values_list('cleaned_team', flat=True).distinct()
        
        # Convert to list and remove any additional whitespace issues
        unique_teams = list(set([team.strip() for team in teams]))
        
        print(unique_teams)  # Debugging output to verify the result
        return Response({'teams': unique_teams})
    

class BaseMagnificentSevenView(APIView):
    def fetch_and_cache_players(self, cache_key, queryset):
        cached_data = cache.get(cache_key)
        if cached_data:
            return cached_data

        best_players = best_of_the_best(queryset)
        response_data = self.build_response_data(best_players)
        cache.set(cache_key, response_data, 600)

        return response_data

    def build_response_data(self, players):
        return [
            {
                'name': f"{player.first_name} {player.last_name}",
                'position': player.position,
                'team': player.team,
                'goals': player.goals,
                'assists': player.assists,
                'clean_sheets': player.clean_sheets,
                'saves': player.saves,
                'penalties_saved': player.penalties_saved,
                'expected_goals_conceded': player.expected_goals_conceded,
                'expected_goal_involvements': player.expected_goal_involvements,
                'creativity': player.creativity,
                'influence': player.influence,
                'threat': player.threat,
                'minutes_played': player.minutes_played,
                'total_points': player.total_points,
                'performance_score': self.calculate_performance_score(player)
            }
            for player in players
        ]

    def calculate_performance_score(self, player):
        match player.position:
            case 'Goalkeeper':
                return calculate_gk_score(player)
            case 'Defender':
                return calculate_def_score(player)
            case 'Midfielder':
                return calculate_mid_score(player)
            case 'Forward':
                return calculate_fwd_score(player)



class MagnificentSevenView(BaseMagnificentSevenView):
    def get(self, request):
        fetch_and_save_players()  # Fetch data from external API and save/update to the database
        
        cache_key = 'magnificent_seven'
        players = Player.objects.all()
        
        response_data = self.fetch_and_cache_players(cache_key, players)
        return Response(response_data)



class MagnificentSevenTeamView(BaseMagnificentSevenView):
    def get(self, request, team_name):
        fetch_and_save_players()  # Fetch data from external API and save/update to the database
        
        cache_key = f'magnificent_seven_{team_name}'
        
        # Perform a case-insensitive filter for the team
        players = Player.objects.filter(team__iexact=team_name)

        if not players.exists():
            return Response({'error': f'No players found for team: {team_name}'}, status=404)
        
        response_data = self.fetch_and_cache_players(cache_key, players)
        return Response(response_data)
