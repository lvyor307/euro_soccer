import numpy as np
import pandas as pd
import re
import requests
from bs4 import BeautifulSoup as Soup


class PlayersDataProvider:
    def __init__(self):
        self.url: str = 'https://sofifa.com/players?offset='
        self.columns = ['ID', 'picture', 'Flag', 'Name', 'Age', 'Position',
                        'Overall', 'Potential', 'Team_Image', 'Team',
                        'Value', 'Wage', 'Total_Point']
        self.df: pd.DataFrame = None

    # set df columns names
    def set_df_col(self, cols):
        self.columns = cols

    # set df
    def set_df(self):
        self.df = pd.DataFrame(columns=self.columns)

    # set url for webscraping
    def set_url(self, url: str):
        self.url: str = url

    def web_scrap(self, offset_limit: int):
        for offset in range(0, offset_limit):
            url = url + str(offset*61)
            p_html = requests.get(self.url)
            p_soup = p_html.text
            data = Soup(p_soup, 'html.parser')
            table = data.find('tbody')
            for i in table.findAll('tr'):
                td = i.findAll('td')
                picture = td[0].find('img').get('data-src')
                ID = td[0].find('img').get('id')
                flag = td[1].find('img').get('data-src')
                Name = td[1].findAll('a')[0].text
                Age = td[2].text.split()
                Position = td[1].findAll('a')[1].text
                Overall = td[3].find('span').text
                Potential = td[4].find('span').text
                Team_image = td[5].find('img').get('data-src')
                Team = td[5].find('a').text
                Value = td[6].text.strip()
                Wage = td[7].text.strip()
                Total_Point = td[8].text.strip()
                player_data = pd.DataFrame([[ID, picture, flag, Name, Age, Position, Overall, Potential,
                                             Team_image, Team, Value, Wage, Total_Point]])

                player_data.columns = self.columns
                self.df = self.df.append(player_data, ignore_index=True)
        self.df = self.df.iloc[self.df.astype(str).drop_duplicates().index]
