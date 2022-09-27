import get_team_links
import get_jsons
import format_games_df
import format_player_df

urls = {'Ballarat' : 'https://nbl1.com.au/fixture?division=men&conference=south&team=ballarat-miners',
        'Bendigo' : 'https://nbl1.com.au/fixture?division=men&conference=south&team=bendigo-braves',
        'Casey' : 'https://nbl1.com.au/fixture?division=men&conference=south&team=casey-cavaliers',
        'Dandenong' : 'https://nbl1.com.au/fixture?division=men&conference=south&team=dandenong-rangers',
        'Diamond_Valley' : 'https://nbl1.com.au/fixture?division=men&conference=south&team=diamond-valley-eagles',
        'Eltham' : 'https://nbl1.com.au/fixture?division=men&conference=south&team=eltham-wildcats',
        'Frankston' : 'https://nbl1.com.au/fixture?division=men&conference=south&team=frankston-blues',
        'Geelong' : 'https://nbl1.com.au/fixture?division=men&conference=south&team=geelong-supercats',
        'Hobart' : 'https://nbl1.com.au/fixture?division=men&conference=south&team=hobart-chargers',
        'Keilor' : 'https://nbl1.com.au/fixture?division=men&conference=south&team=keilor-thunder',
        'Kilsyth' : 'https://nbl1.com.au/fixture?division=men&conference=south&team=kilsyth-cobras',
        'Knox' : 'https://nbl1.com.au/fixture?division=men&conference=south&team=knox-raiders',
        'Melbourne' : 'https://nbl1.com.au/fixture?division=men&conference=south&team=melbourne-tigers',
        'Mt_Gambier' : 'https://nbl1.com.au/fixture?division=men&conference=south&team=mt-gambier-pioneers',
        'Nunawading' : 'https://nbl1.com.au/fixture?division=men&conference=south&team=nunawading-spectres',
        'NW_Tasmania' : 'https://nbl1.com.au/fixture?division=men&conference=south&team=nw-tasmania',
        'Ringwood' : 'https://nbl1.com.au/fixture?division=men&conference=south&team=ringwood-hawks',
        'Sandringham' : 'https://nbl1.com.au/fixture?division=men&conference=south&team=sandringham-sabres',
        'Waverley' : 'https://nbl1.com.au/fixture?division=men&conference=south&team=waverley-falcons'}


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


def main():
    team_games_links = get_team_links.get_team_links(urls)
    game_jsons = get_jsons.get_game_jsons(team_games_links, team_id_dict)
    games_df = format_games_df.create_games_df(game_jsons, team_id_dict)
    player_df = format_player_df.create_player_df(game_jsons, team_id_dict)
    



if __name__ == '__main__':
    main()