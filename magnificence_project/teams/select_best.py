from .score_calculator import *

def best_of_the_best(players): 
    # Set a minimum threshold for minutes played (e.g., 100 minutes)
    min_minutes_played = 150

    # Filter out players with fewer than the minimum minutes played
    gk_candidates = players.filter(position='Goalkeeper', minutes_played__gte=min_minutes_played)
    gk = sorted(gk_candidates, key=calculate_gk_score, reverse=True)[:1]

    defenders = players.filter(position='Defender', minutes_played__gte=min_minutes_played)
    best_defenders = sorted(defenders, key=calculate_def_score, reverse=True)[:2]

    midfielders = players.filter(position='Midfielder', minutes_played__gte=min_minutes_played)
    best_midfielders = sorted(midfielders, key=calculate_mid_score, reverse=True)[:3]

    forwards = players.filter(position='Forward', minutes_played__gte=min_minutes_played)
    best_forward = sorted(forwards, key=calculate_fwd_score, reverse=True)[:1]

    # Combine the selected players into the Magnificent Seven
    magnificent_seven = list(gk) + list(best_defenders) + list(best_midfielders) + list(best_forward)
    
    return magnificent_seven
