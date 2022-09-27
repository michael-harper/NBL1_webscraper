import pandas as pd
from datetime import datetime


def format_player_df(player):
    player_statistics = player['statistics']
    df_player = pd.DataFrame.from_dict([player_statistics]) # have to wrap dictionary in a list for some reason
    if player['starter']:
        df_player.insert(0, "START_POSITION", player['position'])
    else:
        df_player.insert(0, "START_POSITION", "")
    df_player.insert(0, "PLAYER_NAME", player['personName'])
    df_player.insert(0, "PLAYER_ID", player['personId'])
    df_player.insert(0, "TEAM", team_id_dict[player['entityId']])
    df_player.rename(columns = {'assists' : 'AST', 'blocks' : 'BLK', 'efficiency' : 'EFF',
                                'fieldGoalsAttempted' : 'FGA', 'fieldGoalsMade' : 'FGM', 'fieldGoalsPercentage' : 'FG_PCT',
                                'foulsTotal' : 'PF', 'freeThrowsAttempted' : 'FTA', 'freeThrowsMade' : 'FTM',
                                'freeThrowsPercentage' : 'FT_PCT', 'minutes' : 'MIN', 'plusMinus' : 'PLUS_MINUS',
                                'points' : 'PTS', 'pointsThreeAttempted' : 'FG3A', 'pointsThreeMade' : 'FG3M', 'pointsThreePercentage' : 'FG3_PCT',
                                'pointsTwoAttempted' : 'FG2A', 'pointsTwoMade' : 'FG2M', 'pointsTwoPercentage' : 'FG2_PCT', 'rebounds' : 'REB',
                                'reboundsDefensive' : 'DREB', 'reboundsOffensive' : 'OREB', 'steals' : 'STL', 'turnovers' : 'TO'
                                }, inplace=True)
    
    return df_player

player_frames = []
for game in game_jsons:
    game_id = game['data']['fixture']['fixtureId']
    for player in game['data']['statistics']['home']['persons']:
        df = format_player_df(player)
        df.insert(0, "GAME_ID", game_id)
        min_sec = df['MIN'].to_string()[1:].strip().split("M")
        minutes = int(''.join([i for i in min_sec[0] if i.isdigit()]))
        if min_sec[1] == '':
            sec = 0
        else:
            sec = int(''.join([i for i in min_sec[1] if i.isdigit()]))
        minsec = str(minutes) + ':' + str(sec)
        df['MIN'] = minsec
        # df['MIN'] = pd.to_datetime(minsec, format='%M:%S').time
        df.insert(0, "Game_Date", pd.to_datetime(game['data']['fixture']['startTimeLocal']))
        player_frames.append(df) 

final_player_df = pd.concat(player_frames, ignore_index=True)    

# Write to CSV
final_player_df.to_csv('/Users/Michael/Documents/Waverley/player_stats.csv')