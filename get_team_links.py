from selenium import webdriver
from selenium.webdriver.support.ui import Select 
from bs4 import BeautifulSoup
import time
import pandas as pd
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from collections import defaultdict
import pandas as pd

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


def get_team_links(urls):
    driver = webdriver.Chrome('chromedriver')
    driver.implicitly_wait(3)
    teams_game_links = defaultdict(list)
    for k,v in urls.items():
        url = v
        driver.get(url)
        time.sleep(7)
        elems = driver.find_elements_by_tag_name('a')
        game_links = []  
        for elem in elems:
            href = elem.get_attribute('href')
            if href is not None:
                if 'games' in href:
                    if href not in game_links:
                        game_links.append(href)
        teams_game_links[k] += game_links
    return teams_game_links

    
