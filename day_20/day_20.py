# Read this url and find the 10 most frequent words.
# romeo_and_juliet = 'https://www.gutenberg.org/cache/epub/1513/pg1513.txt'

import re
from collections import Counter

import requests

url = 'https://www.gutenberg.org/cache/epub/1513/pg1513.txt'

response = requests.get(url)  # fetch the plain text
response.raise_for_status()   # stop with a clear error if the request failed

words = re.findall(r"[a-z']+", response.text.lower())

for word, count in Counter(words).most_common(10):
    print(count, word)

# Read the cats API and cats_api = 'https://api.thecatapi.com/v1/breeds' and find :

# 1. the min, max, mean, median, standard deviation of cats' weight in metric units.
from keys import CATS_API_KEY, COUNTRIES_API_KEY
from statistics import mean, median, stdev
API_URL = 'https://api.thecatapi.com/v1/breeds'

response = requests.get(API_URL, headers={'x-api-key': CATS_API_KEY})

cats = response.json()
weights = []
for cat in cats:
    try:
        parts = [float(p) for p in cat['weight']['metric'].split('-')]
    except ValueError:  # a few breeds have text instead of a weight
        continue
    weights.append(sum(parts) / len(parts))  # mean of the range (or the single value)

print('Cats min weight is:', min(weights))
print('Cats max weight is:', max(weights))
print('Cats mean weight is:', mean(weights))
print('Cats median weight is:', median(weights))
print('Cats standard deviation of weight is:', stdev(weights))

# 2. the min, max, mean, median, standard deviation of cats' lifespan in years.
lifespans = []
for cat in cats:
    parts = [float(p) for p in cat['life_span'].split('-')]
    lifespans.append(sum(parts) / len(parts))

print('Cats min lifespan is:', min(lifespans))
print('Cats max lifespan is:', max(lifespans))
print('Cats mean lifespan is:', mean(lifespans))
print('Cats median lifespan is:', median(lifespans))
print('Cats standard deviation of lifespan is:', stdev(lifespans))

# 3. Create a frequency table of country and breed of cats
# (some breeds have no origin, so they are skipped in the table)
origins = Counter(cat['origin'] for cat in cats if cat.get('origin'))
print('Country   Breeds')
for origin, count in origins.most_common():
    print(f'{origin:<30}{count}')

# Read the countries API and find
# the 10 largest countries
# the 10 most spoken languages
# the total number of languages in the countries API
url = "https://api.restcountries.com/countries/v5"
headers = {'Authorization': f'Bearer {COUNTRIES_API_KEY}'}

# the API is paginated (25 by default, 100 max on the free plan), so ask page by page
countries = []
offset = 0
while True:
    params = {"fields": "names,area,languages", "limit": 100, "offset": offset}
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    data = response.json()['data']
    countries += data['objects']
    if not data['meta']['more']:
        break
    offset += 100

# 1. the 10 largest countries (area is a dict: {'kilometers': ..., 'miles': ...})
largest = sorted(countries, key=lambda c: c['area']['kilometers'], reverse=True)[:10]
for country in largest:
    print(country['area']['kilometers'], country['names']['common'])

# 2. the 10 most spoken languages (here: spoken in the most countries)
language_counts = Counter(
    language['name'] for country in countries for language in country['languages']
)
for language, count in language_counts.most_common(10):
    print(count, language)

# 3. the total number of languages in the countries API
print('Total number of languages:', len(language_counts))

# UCI is one of the most common places to get data sets for data science and machine learning.
# Read the content of UCL (https://archive.ics.uci.edu/ml/datasets.php).
# The old url redirects to https://archive.ics.uci.edu/datasets, and the links to
# every data set (/dataset/<id>/<name>) are already in the HTML, so BeautifulSoup is enough.
from bs4 import BeautifulSoup

uci_url = 'https://archive.ics.uci.edu/datasets'

response = requests.get(uci_url, headers={'User-Agent': 'Mozilla/5.0'})
response.raise_for_status()

soup = BeautifulSoup(response.text, 'html.parser')
links = soup.select('a[href^="/dataset/"]')

# every data set appears more than once (image link + title link), so keep the unique ones
datasets = {link['href']: link.get_text(strip=True) for link in links}
datasets = {href: name for href, name in datasets.items() if name}

print('Data sets in the first page of UCI:', len(datasets))
for href, name in list(datasets.items())[:10]:
    print(name, '->', 'https://archive.ics.uci.edu' + href)
