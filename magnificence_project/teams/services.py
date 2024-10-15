import requests
from .models import Player
import os
from dotenv import load_dotenv
from django.db import transaction

load_dotenv()

API_URL = os.getenv("MAGNIFICENT_API")

# Map element_type to human-readable positions
POSITION_MAP = {
    1: 'Goalkeeper',
    2: 'Defender',
    3: 'Midfielder',
    4: 'Forward',
}


def fetch_and_save_players():
    """Fetches player data and saves it to the database."""
    data = fetch_data()
    team_map = build_team_map(data)
    if team_map:
        players_data = filter_players_data(data)
        if players_data:
            save_player_data_bulk(players_data, team_map)


def fetch_data():
    """Fetches data"""
    try:
        response = requests.get(API_URL)
        response.raise_for_status()
        return response
    except requests.RequestException as e:
            print(f"Error fetching data: {e}")
            return None


def build_team_map(data):
    """Builds a dynamic map of team IDs to team names."""
    teams_data = filter_teams_data(data)
    team_map = {}
    for team in teams_data:
        team_id = team['id']
        team_name = team['name']
        team_map[team_id] = team_name
    return team_map


def filter_players_data(data):
    """Filter the player data."""
    return data.json().get('elements', [])


def filter_teams_data(data):
    """Filter the teams data."""
    return data.json().get('teams', [])


def save_player_data_bulk(players_data, team_map):
    """Saves or updates player data in bulk to the database."""
    players_to_create = []
    players_to_update = []

    for player in players_data:
        player_id = player.get('id')
        first_name = player.get('first_name', '')
        last_name = player.get('second_name', '')
        position = POSITION_MAP.get(player.get('element_type'), 'Unknown')
        team_id = player.get('team')
        team = team_map.get(team_id, f"Team {team_id}")
        minutes = player.get("minutes", 0)
        goals = player.get('goals_scored', 0)
        assists = player.get('assists', 0)
        clean_sheets = player.get('clean_sheets', 0)
        saves = player.get('saves', 0)
        goals_conceded = player.get('goals_conceded', 0)
        yellow_cards = player.get('yellow_cards', 0)
        red_cards = player.get('red_cards', 0)
        penalties_saved = player.get('penalties_saved', 0)
        influence = player.get('influence', 0.0)
        creativity = player.get('creativity', 0.0)
        threat = player.get('threat', 0.0)
        expected_goals = player.get('expected_goals', 0.0)
        expected_assists = player.get('expected_assists', 0.0)
        expected_goal_involvements = player.get('expected_goal_involvements', 0.0)
        expected_goals_conceded = player.get('expected_goals_conceded', 0.0)
        total_points = player.get('total_points', 0)

        # Check if player exists, add to update list or create list
        try:
            existing_player = Player.objects.get(player_id=player_id)
            existing_player.first_name = first_name
            existing_player.last_name = last_name
            existing_player.position = position
            existing_player.team = team
            existing_player.minutes_played = minutes
            existing_player.goals = goals
            existing_player.assists = assists
            existing_player.clean_sheets = clean_sheets
            existing_player.saves = saves
            existing_player.goals_conceded = goals_conceded
            existing_player.yellow_cards = yellow_cards
            existing_player.red_cards = red_cards
            existing_player.penalties_saved = penalties_saved
            existing_player.influence = influence
            existing_player.creativity = creativity
            existing_player.threat = threat
            existing_player.expected_goals = expected_goals
            existing_player.expected_assists = expected_assists
            existing_player.expected_goal_involvements = expected_goal_involvements
            existing_player.expected_goals_conceded = expected_goals_conceded
            existing_player.total_points = total_points

            players_to_update.append(existing_player)
        except Player.DoesNotExist:
            players_to_create.append(Player(
                player_id=player_id,
                first_name=first_name,
                last_name=last_name,
                position=position,
                team=team,
                minutes_played=minutes,
                goals=goals,
                assists=assists,
                clean_sheets=clean_sheets,
                saves=saves,
                goals_conceded=goals_conceded,
                yellow_cards=yellow_cards,
                red_cards=red_cards,
                penalties_saved=penalties_saved,
                influence=influence,
                creativity=creativity,
                threat=threat,
                expected_goals=expected_goals,
                expected_assists=expected_assists,
                expected_goal_involvements=expected_goal_involvements,
                expected_goals_conceded=expected_goals_conceded,
                total_points=total_points
            ))

    # Use bulk_create for new players
    if players_to_create:
        Player.objects.bulk_create(players_to_create, ignore_conflicts=True)

    # Update existing players in a transaction for efficiency
    if players_to_update:
        with transaction.atomic():
            Player.objects.bulk_update(players_to_update, [
                'first_name', 'last_name', 'position', 'team', 'minutes_played',
                'goals', 'assists', 'clean_sheets', 'saves', 'goals_conceded',
                'yellow_cards', 'red_cards', 'penalties_saved', 'influence',
                'creativity', 'threat', 'expected_goals', 'expected_assists',
                'expected_goal_involvements', 'expected_goals_conceded', 'total_points'
            ])
