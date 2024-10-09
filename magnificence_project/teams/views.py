from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.cache import cache
from .models import Player
from .services import fetch_and_save_players

class MagnificentSevenView(APIView):
    def get(self, request):
        fetch_and_save_players()  # Fetch data from external API and save/update to the database

        cache_key = 'magnificent_seven'
        cached_data = cache.get(cache_key)

        if cached_data:
            return Response(cached_data)

        # Goalkeeper (GK)
        def calculate_gk_score(player):
            score = 0
            score += player.saves * 20
            score += player.clean_sheets * 15
            score -= player.goals_conceded * 30
            score += player.penalties_saved * 30
            score -= player.expected_goals_conceded * 5

            if player.minutes_played >= 250:
                score += 15
            elif player.minutes_played >= 100:
                score += 10

            return score

        # Defender (DEF)
        def calculate_def_score(player):
            score = 0
            score += player.goals * 20
            score += player.assists * 15
            score += player.clean_sheets * 30
            score -= player.goals_conceded * 10
            score -= player.expected_goals_conceded * 5

            return score

        # Midfielder (MID)
        def calculate_mid_score(player):
            score = 0
            score += player.goals * 25
            score += player.assists * 20

            if player.creativity > 100:
                score += 5

            if player.influence > 200:
                score += 5

            score += player.expected_goal_involvements * 5
            score += player.expected_assists * 5

            if player.minutes_played >= 250:
                score += 15
            elif player.minutes_played >= 100:
                score += 10

            return score

        # Forward (FWD)
        def calculate_fwd_score(player):
            score = 0
            score += player.goals * 35
            score += player.assists * 15

            if player.threat > 200:
                score += 15

            if player.influence > 200:
                score += 5

            score += player.expected_goal_involvements * 10
            score += player.expected_goals * 20
            score += player.expected_assists * 15

            return score

        players = Player.objects.all()

        # Select the best goalkeeper
        gk_candidates = players.filter(position='Goalkeeper')
        gk = sorted(gk_candidates, key=calculate_gk_score, reverse=True)[:1]

        # Select the best defenders
        defenders = sorted(players.filter(position='Defender'), key=calculate_def_score, reverse=True)[:2]

        # Select the best midfielders
        midfielders = sorted(players.filter(position='Midfielder'), key=calculate_mid_score, reverse=True)[:3]

        # Select the best forward
        forward = sorted(players.filter(position='Forward'), key=calculate_fwd_score, reverse=True)[:1]

        # Combine
        magnificent_seven = list(gk) + list(defenders) + list(midfielders) + list(forward)

        response_data = [
            {
                'name': f"{player.first_name} {player.last_name}",
                'position': player.position,
                'team': player.team,
                'goals': player.goals,
                'assists': player.assists,
                'clean_sheets': player.clean_sheets,
                'saves': player.saves if player.position == 'Goalkeeper' else 0,
                'penalties_saved': player.penalties_saved if player.position == 'Goalkeeper' else None,
                'expected_goals_conceded': player.expected_goals_conceded,
                'expected_goal_involvements': player.expected_goal_involvements if player.position in ['Midfielder', 'Forward'] else None,
                'creativity': player.creativity if player.position == 'Midfielder' else None,
                'influence': player.influence,
                'threat': player.threat if player.position == 'Forward' else None,
                'minutes_played': player.minutes_played,
                'total_points': player.total_points,
                'performance_score': calculate_gk_score(player) if player.position == 'Goalkeeper' else (
                    calculate_def_score(player) if player.position == 'Defender' else (
                        calculate_mid_score(player) if player.position == 'Midfielder' else calculate_fwd_score(player)
                    )
                )
            }
            for player in magnificent_seven
        ]

        cache.set(cache_key, response_data, 600)

        return Response(response_data)
