# This is a sample Python script.
import pprint

from bs4 import BeautifulSoup
import requests
import pandas as pd
url = 'https://it.iiita.ac.in/?pg=faculty'
data = requests.get(url)
html = data.text
soup = BeautifulSoup(html, 'html.parser')
div = soup.find('div', {'id': 'tooplate_main'})
table = div.find('table')
ans = []
for tr in table.find_all('tr'):
    obj = {}
    td_list = tr.find_all('td')
    if len(td_list) <= 1:
        continue
    for td in td_list:
        txt = td.text.strip()
        if txt:
            values = [t.strip() for t in txt.split('\n')]
            obj['name'] = values[0]
            if values[1]:
                obj['position'] = values[1]
            obj['qualifications'] = values[2]
            interests = values[3].split('Research Interests:')[1]
            if interests:
                obj['interests'] = interests
        ans.append(obj)
        pprint.pprint(ans, indent=4, width=100)
