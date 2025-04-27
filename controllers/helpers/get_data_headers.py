from nba_api.stats.endpoints import playerfantasyprofile
from nba_api.stats.static import players

import random

def get_data_headers(dataset):
    match dataset:
        case 'player_fantasy_profile':
            get_profile_headers = playerfantasyprofile.PlayerFantasyProfile(player_id=get_random_active_player_id())
            return get_profile_headers.overall.data['headers']
        case _:
            print(f"nothing to show here: {dataset}")


def get_random_active_player_id():
    all_active_players = players.get_active_players()
    random_i = random.randint(0, len(all_active_players))
    player_id = all_active_players[random_i]['id']

    return player_id
    