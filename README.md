# Fast Break
## The game of fast basketball fantasy management

This is hopefully a simple game project for the CLI, written in Python.
The idea is you're given a set budget and must draft NBA players to compete in a fantasy game against the
'computer' (RNG). This is done within a set time limit and using a rating system based on latest player stats
obtained from an open source API.

***
## The plan
The plan of development is currently in the following order, but as I work through this, it will inevitably
change.

1. Find relevant API endpoints ([nba_api](https://github.com/swar/nba_api/tree/master))
2. Test obtaining data and format data schemas for use in game
3. Decide on a rating/valuation system dependant on player stats/data
4. Build the CLI
5. Determine draft system
6. Determine scoring system
7. Play game

***

## Diary
### Day two - 2.5 Hours
Got basic dictionary to csv system working using nba api endpoints.
Had to use ChatGPT for guidance on converting the 2 separate lists as a dictionary that pandas could use.

TODO: 
* Decide on a simple rating system and way to value the players
* Tidy up unnecessary testing files from project

### Day one ~ 1 Hour
Scaffolded basic project, initialised git and virtual environment.
Installed nba_api.
Began testing the endpoints.

ToDo:
* Batch download all player splits from API
* Store as CSV file
* This is to reduce the amount of API calls needed
* Serve as local database of data
* Will introduce an option to download latest stats or use saved

