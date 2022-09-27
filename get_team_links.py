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

    