from nba_api.stats.static import players, teams
from nba_api.stats.endpoints import playerdashboardbylastngames
import pprint


all_players = players.get_active_players()
all_teams = teams.get_teams()

player_id = 1628386 # get player id from all_players info
num_games = 6

player_info = playerdashboardbylastngames.PlayerDashboardByLastNGames(
    player_id=player_id,
    last_n_games=num_games
    )

last_5_games = player_info.last5_player_dashboard.data["data"][0]
last_5_headers = player_info.last5_player_dashboard.data["headers"]

for i in range(len(last_5_games)):
    print(f"{last_5_headers[i]} - {last_5_games[i]}")



# for i in range(0, 10):
#     print(all_players[i])
