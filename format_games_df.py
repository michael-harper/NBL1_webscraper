import pandas as pd
from datetime import datetime

def format_df(json, team_id_dict):
    df_home = pd.json_normalize(json['data']['statistics']['home']['entity'])
    df_away = pd.json_normalize(json['data']['statistics']['away']['entity'])
    df_home.rename(columns= {'assists' : 'AST_Home', 'blocks' : 'BLKS_Home', 'efficiency' : 'EFF_Home', 
                    'fieldGoalsAttempted' : 'FGA_Home', 'fieldGoalsMade' : 'FGM_Home', 'fieldGoalsPercentage' : 'FG_PCT_Home',
                    'foulsTotal' : 'FOULS_Home', 'freeThrowsAttempted' : 'FTA_Home', 'freeThrowsMade' : 'FTM_Home',
                    'freeThrowsPercentage' : 'FT_PCT_Home', 'pointsThreeAttempted' : 'FG3A_Home',
                    'pointsThreeMade' : 'FG3M_Home', 'pointsThreePercentage' : 'FG3_PCT_Home', 'pointsTwoAttempted' : 'FG2A_Home',
                    'pointsTwoMade' : 'FG2M_Home', 'pointsTwoPercentage' : 'FG2_PCT_Home', 'rebounds' : 'REB_Home', 
                    'reboundsDefensive' : 'DREB_Home', 'reboundsOffensive' : 'OREB_Home', 'steals' : 'STL_Home',
                    'turnovers' : 'TO_Home'}, inplace=True)
    df_home.insert(0, "PTS_Home", json['data']['fixture']['competitors'][0]['score'])
    df_home.drop(['points', 'minutes', 'plusMinus'], inplace=True, axis=1)
    df_away.rename(columns= {'assists' : 'AST_Away', 'blocks' : 'BLKS_Away', 'efficiency' : 'EFF_Away', 
                    'fieldGoalsAttempted' : 'FGA_Away', 'fieldGoalsMade' : 'FGM_Away', 'fieldGoalsPercentage' : 'FG_PCT_Away',
                    'foulsTotal' : 'FOULS_Away', 'freeThrowsAttempted' : 'FTA_Away', 'freeThrowsMade' : 'FTM_Away',
                    'freeThrowsPercentage' : 'FT_PCT_Away', 'pointsThreeAttempted' : 'FG3A_Away',
                    'pointsThreeMade' : 'FG3M_Away', 'pointsThreePercentage' : 'FG3_PCT_Away', 'pointsTwoAttempted' : 'FG2A_Away',
                    'pointsTwoMade' : 'FG2M_Away', 'pointsTwoPercentage' : 'FG2_PCT_Away', 'rebounds' : 'REB_Away', 
                    'reboundsDefensive' : 'DREB_Away', 'reboundsOffensive' : 'OREB_Away', 'steals' : 'STL_Away',
                    'turnovers' : 'TO_Away'}, inplace=True)
    df_away.insert(0, "PTS_Away", json['data']['fixture']['competitors'][1]['score'])
    df_away.drop(['points', 'minutes', 'plusMinus'], inplace=True, axis=1)
    df = pd.concat([df_home, df_away], axis=1)
    df.insert(0, "AWAY_TEAM_ID", team_id_dict[json['data']['fixture']['competitors'][1]['entityId']])
    df.insert(0, "HOME_TEAM_ID", team_id_dict[json['data']['fixture']['competitors'][0]['entityId']])
    df.insert(0, "GAMIE_ID", json['data']['fixture']['fixtureId'])
    df.insert(0, "Game_Date", pd.to_datetime(json['data']['fixture']['startTimeLocal']))
    if json['data']['fixture']['competitors'][0]['resultPlace'] == 1:
        df['HOME_TEAM_WINS'] = json['data']['fixture']['competitors'][0]['resultPlace']
    else:
        df['HOME_TEAM_WINS'] = 0

    return df

# Create list of df's first and concatenate at end, much faster this way
def create_games_df(game_jsons, team_id_dict):
    frames = []
    for game in game_jsons:
        present = datetime.now()
        if pd.to_datetime(game['data']['fixture']['startTimeLocal']) > present:
            continue
        frames.append(format_df(game, team_id_dict))
    final_games_df = pd.concat(frames, ignore_index=True)
    
    return final_games_df

#Write to CSV File
# final_games_df.to_csv('/Users/Michael/Documents/Waverley/games.csv')