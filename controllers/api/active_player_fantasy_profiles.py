from nba_api.stats.static import players
from controllers.api.get_player_fantasy_profile_data import get_player_fantasy_profile_data
from controllers.helpers.get_data_headers import get_data_headers
from controllers.helpers.write_dict_to_csv import write_dict_to_csv
from controllers.helpers.convert_data_to_dicts import convert_data_to_dicts

def active_player_fantasy_profiles():
    player_data = players.get_active_players()

    active_player_data = []

    headers = get_data_headers('player_fantasy_profile')
    headers.insert(0, 'PLAYER ID')

    for i in range(0,3):
        player_id = player_data[i]['id']
        player_stats = get_player_fantasy_profile_data(player_id=player_id)
        player_stats.insert(0,player_id)

        active_player_data.append(player_stats)

    # print(type(headers), " : ", headers)
    # print(type(active_player_data), " : ", active_player_data)
    
    player_data_dict = convert_data_to_dicts(headers, active_player_data)
    print(player_data_dict)

    write_dict_to_csv(player_data_dict, 'testing_dw1')