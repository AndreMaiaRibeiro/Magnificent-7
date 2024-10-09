# Goalkeeper (GK)
def calculate_gk_score(player):
    score = 0
    score += player.saves * 20
    score += player.clean_sheets * 15
    score -= player.goals_conceded * 30
    score += player.penalties_saved * 30
    score -= player.expected_goals_conceded * 5

    return score

# Defender (DEF)
def calculate_def_score(player):
    score = 0
    score += player.goals * 20
    score += player.assists * 15
    score += player.clean_sheets * 30
    score -= player.goals_conceded * 2
    score -= player.expected_goals_conceded * 1
    if player.influence > 100:
        score += 20
        
    if player.threat > 50:
        score += 20
    
    if player.creativity > 50:
            score += 20

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

    score += player.expected_goal_involvements * 50
    score += player.expected_assists * 20

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