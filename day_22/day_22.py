# Exercises: Day 22
import json
import re

import requests
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0'}

# 1. Scrape the following website and store the data as json file
url = 'http://www.bu.edu/president/boston-university-facts-stats/'

response = requests.get(url, headers=headers)
print(response.status_code)
response.raise_for_status()

soup = BeautifulSoup(response.content, 'html.parser')

bu_stats = []
for item in soup.find_all('article', class_='bu-stat-single'):
    title = item.find('h3', class_='bu-stat-title').get_text(strip=True)
    value = ''.join(
        s.get_text(strip=True)
        for s in item.select('.bu-stat-prefix, .bu-stat-value, .bu-stat-suffix')
    )
    bu_stats.append({'title': title, 'value': value})

print(bu_stats)

with open('bu_stats.json', 'w', encoding='utf-8') as f:
    json.dump(bu_stats, f, indent=4, ensure_ascii=False)

# 2. Extract the table in this url (https://archive.ics.uci.edu/ml/datasets.php)
# and change it to a json file
# The page is now rendered with JavaScript and the old .php url returns 404, so
# the HTML has no <table>. The table is filled from this JSON API instead.
url = 'https://archive.ics.uci.edu/api/datasets/list'

response = requests.get(url, headers=headers)
print(response.status_code)
response.raise_for_status()

uci_datasets = response.json()['data']
print(len(uci_datasets), uci_datasets[:3])

with open('uci_datasets.json', 'w', encoding='utf-8') as f:
    json.dump(uci_datasets, f, indent=4, ensure_ascii=False)

# 3. Scrape the presidents table and store the data as json
url = 'https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States'

response = requests.get(url, headers=headers)
print(response.status_code)
response.raise_for_status()

soup = BeautifulSoup(response.content, 'html.parser')
table = soup.find('table', class_='wikitable')


def clean(cell):
    # remove footnote markers such as [ a ] or [ 19 ]
    text = cell.get_text(' ', strip=True)
    return re.sub(r'\s*\[\s*\w+\s*\]', '', text).strip()


presidents = []
for row in table.find_all('tr')[1:]:
    cells = row.find_all(['th', 'td'])
    # rows with rowspan (second term) only have the election cell, skip them
    if len(cells) < 7:
        continue
    presidents.append({
        'number': clean(cells[0]),
        'name': clean(cells[2]),
        'term': clean(cells[3]),
        'party': clean(cells[5]),
        'election': clean(cells[6]),
        'vice_president': clean(cells[7]) if len(cells) > 7 else '',
    })

print(len(presidents), presidents[:2])

with open('presidents.json', 'w', encoding='utf-8') as f:
    json.dump(presidents, f, indent=4, ensure_ascii=False)
