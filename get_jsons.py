import requests


team_id_dict = {
    "dea43458-7b55-11eb-9e56-8205bb8987e9" : "Ballarat",
    "decbdaa8-7b55-11eb-9e56-8205bb8987e9" : "Geelong",
    "df02e2e6-7b55-11eb-9e56-8205bb8987e9" : "Nunawading",
    "deb719a6-7b55-11eb-9e56-8205bb8987e9" : "Dandenong",
    "df18d768-7b55-11eb-9e56-8205bb8987e9" : "Sandringham",
    "dea89804-7b55-11eb-9e56-8205bb8987e9" : "Bendigo",
    "debae9be-7b55-11eb-9e56-8205bb8987e9" : "Diamond Valley",
    "dee45eb6-7b55-11eb-9e56-8205bb8987e9" : "Knox",
    "df0f8960-7b55-11eb-9e56-8205bb8987e9" : "Ringwood",
    "def3ca86-7b55-11eb-9e56-8205bb8987e9" : "Melbourne",
    "df464d6a-7b55-11eb-9e56-8205bb8987e9" : "Waverley",
    "def6b48a-7b55-11eb-9e56-8205bb8987e9" : "Mt Gambier",
    "df047958-7b55-11eb-9e56-8205bb8987e9" : "NW Tasmania",
    "dec341f4-7b55-11eb-9e56-8205bb8987e9" : "Eltham",
    "2d6ba6fc-2ccc-11ec-87a0-823dda86fdf0" : "Keilor",
    "dec8ed0c-7b55-11eb-9e56-8205bb8987e9" : "Frankston",
    "ded5e0d4-7b55-11eb-9e56-8205bb8987e9" : "Hobart",
    "dee186dc-7b55-11eb-9e56-8205bb8987e9" : "Kilsyth",
    "cf56df1e-2ccb-11ec-956b-5a830b91402e" : "Casey"
}


# Unique Games Played
unique_games = []
for team, game_list in teams_game_links.items():
    for game in game_list:
        game_id = game[26:]
        if game_id not in unique_games:
            unique_games.append(game_id)


# JSON's of Games Played
api_url = 'https://eapi.web.prod.cloud.atriumsports.com/v1/embed/3/fixtures/'
api_stats = '/statistics?sub=statistics'
game_jsons = []

for game in unique_games:
    game_id = game
    game_api = api_url + game_id + api_stats
    print(game_api)
    response = requests.get(game_api)
    game_jsons.append(response.json())