from nba_api.stats.endpoints import playerfantasyprofile

def get_player_fantasy_profile_data(player_id):
    get_player_data = playerfantasyprofile.PlayerFantasyProfile(player_id=player_id)
    
    player_stats = get_player_data.overall.data['data'][0]

    return player_stats

