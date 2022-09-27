import requests

def get_game_jsons(teams_game_links):
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

    return game_jsons