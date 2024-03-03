# Scrapes the data for goals and assists from wikipedia

from requests import get
from bs4 import BeautifulSoup
import json


class scrape_table:

    def __init__(self, website, index):
        request = get(website)
        soup = BeautifulSoup(request.text,'html.parser')

        self.table = soup.find_all('table', class_='wikitable')[index-1]
        self.players = self.table.find_all('tr')[1:]


    def remove(self, s):
        s = s.strip()
        s = s.strip('\n')
        return s


    def is_int(self, string):
        try:
            int(string)
            return True
        except:
            return False


    def get_list(self):
        data = []

        for player in self.players:
            stats = player.find_all(['th','td'])
            stats = [self.remove(i.text) for i in stats]
            try:
                img = player.find_all('img')[0]
            except IndexError:
                break
            stats.append(img['alt'])
            stats.append('https:' + img['src'])
            data.append(stats)


        for i in data:
            if self.is_int(i[0]):
                del i[0]
            if self.is_int(i[2]):
                goals = i[2]
            else:
                i.insert(2,int(goals))

        return data


    def get_obj(self):
        x = self.get_list()
        obj = []
        for i in x:
            obj.append({
                'name': i[0],
                'club': i[1],
                'amount': i[2],
                'nation': i[3],
                'flag': i[4]
            })
        return obj

epl_goals = scrape_table('https://en.wikipedia.org/wiki/2018%E2%80%9319_Premier_League', 6)
epl_assists = scrape_table('https://en.wikipedia.org/wiki/2018%E2%80%9319_Premier_League', 8)

with open('epl_goals.json', 'w+') as f:
    json.dump(epl_goals.get_obj(), f, indent=2)

with open('epl_assists.json', 'w+') as f:
    json.dump(epl_assists.get_obj(), f, indent=2)

seriea_goals = scrape_table('https://en.wikipedia.org/wiki/2018–19_Serie_A', 7)
seriea_assists = scrape_table('https://en.wikipedia.org/wiki/2018–19_Serie_A', 8)

with open('seriea_goals.json', 'w+') as f:
    json.dump(seriea_goals.get_obj(), f, indent=2)

with open('seriea_assists.json', 'w+') as f:
    json.dump(seriea_assists.get_obj(), f, indent=2)

laliga_goals = scrape_table('https://en.wikipedia.org/wiki/2018%E2%80%9319_La_Liga', 7)
laliga_assists = scrape_table('https://en.wikipedia.org/wiki/2018%E2%80%9319_La_Liga', 8)

with open('laliga_goals.json', 'w+') as f:
    json.dump(laliga_goals.get_obj(), f, indent=2)

with open('laliga_assists.json', 'w+') as f:
    json.dump(laliga_assists.get_obj(), f, indent=2)

mls_goals = scrape_table("https://en.wikipedia.org/wiki/2018_Major_League_Soccer_season", 12)
mls_assists = scrape_table("https://en.wikipedia.org/wiki/2018_Major_League_Soccer_season", 13)

with open('mls_goals.json', 'w+') as f:
    json.dump(mls_goals.get_obj(), f, indent=2)

with open('mls_assists.json', 'w+') as f:
    json.dump(mls_assists.get_obj(), f, indent=2)

ligue1_goals = scrape_table("https://en.wikipedia.org/wiki/2018-19_Ligue_1", 8)
ligue1_assists = scrape_table("https://en.wikipedia.org/wiki/2018-19_Ligue_1", 9)

with open('ligue1_goals.json', 'w+') as f:
    json.dump(ligue1_goals.get_obj(), f, indent=2)

with open('ligue1_assists.json', 'w+') as f:
    json.dump(ligue1_assists.get_obj(), f, indent=2)
