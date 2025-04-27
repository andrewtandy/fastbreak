from nba_api.stats.endpoints import playercareerstats
from nba_api.stats.endpoints import playerdashboardbylastngames
from nba_api.stats.endpoints import playerdashboardbygamesplits
from nba_api.stats.endpoints import playerfantasyprofile

import pandas as pd

import pprint

career = playercareerstats.PlayerCareerStats(player_id='203999')

player_id = '203999'
num_games = 20

player_fantasy= playerfantasyprofile.PlayerFantasyProfile(
    player_id=player_id,
    # last_n_games=num_games
)

# player_info = playerdashboardbylastngames.PlayerDashboardByLastNGames(
#     player_id=player_id,
#     last_n_games=num_games
# )

headers = player_fantasy.overall.data['headers']
stats = player_fantasy.overall.data['data'][0]

# headers = player_info.last5_player_dashboard.get_dict()['headers']
# last_5 = player_info.last5_player_dashboard.get_dict()['data'][0]
# last_10 = player_info.last10_player_dashboard.get_dict()['data'][0]
# last_20 = player_info.last20_player_dashboard.get_dict()['data'][0]



data = {}


for i in range(len(headers)):
    data[headers[i]] = [stats[i]]

df = pd.DataFrame(data)

csv_file_path = 'data_game_splits.csv'

df.to_csv(csv_file_path, index=False)


