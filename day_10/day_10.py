# Exercises: Day 10
# Level 1
# Iterate 0 to 10 using for loop, do the same using while loop

for number in range(11):
    print(number)

count = 1
while count < 11:
    print(count)
    count = count + 1
    if count == 11:
        break

# Iterate 10 to 0 using for loop, do the same using while loop.
for number in range(10, -1, -1):
    print(number)

count = 10
while count >= 0:
    print(count)
    count = count - 1
    if count == -1:
        break

# Write a loop that makes seven calls to print(), so we get on the output 
# the following triangle:
triangle = '#'
for number in range(7):
    print(triangle)
    triangle = triangle + '#'

# Use nested loops to create the following:
for row in range(8):
    for col in range(8):
        print('#', end=' ')
    print()

# Print the following pattern
for row in range(11):
    print(f'{row} x {row} = {row*row}')

# Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] 
# using a for loop and print out the items.
skills = ['Python', 'Numpy','Pandas','Django', 'Flask'] 

for skill in skills:
    print(skill)

# Use for loop to iterate from 0 to 100 and print only even numbers
for number in range(101):
    if number%2 == 0:
        print(number)

# Use for loop to iterate from 0 to 100 and print only odd numbers
for number in range(101):
    if number%2 != 0:
        print(number)

# Level 2
# Use for loop to iterate from 0 to 100 and print the sum of all numbers.
suma=0
for number in range(101):
    suma = suma + number

print(f'The sum of all numbers is is {suma}')

# Use for loop to iterate from 0 to 100 and print the sum of all evens 
# and the sum of all odds.
sum_of_evens = 0
sum_of_odds = 0
for number in range(101):
    if number%2 == 0:
        sum_of_evens = sum_of_evens + number
    else:
        sum_of_odds = sum_of_odds + number

print(f'The sum of all evens is {sum_of_evens}. And the sum of all odds is {sum_of_odds}')

# Level 3
# Go to the data folder and use the countries.py file. 
# Loop through the countries and extract all the countries 
# containing the word land.

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from data.countries import countries

land_lt = list()
for country in countries:
    if 'land' in country:
        land_lt.append(country)

print(land_lt)

# This is a fruit list, 
# ['banana', 'orange', 'mango', 'lemon'] 
# reverse the order using loop.
fruits = ['banana', 'orange', 'mango', 'lemon']
reversed_fruits=[] 
for fruit in fruits:
    reversed_fruits.insert(0,fruit)

print(reversed_fruits)

# Go to the data folder and use the countries_data.py file.
# What are the total number of languages in the data
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from data.countries_data import countries_data
count_countries = 0
for country in countries_data:
    count_countries += len(country['languages'])

print(f'The number of languages in countries_data is', count_countries)

# Find the ten most spoken languages from the data
conteo = dict()
for country in countries_data:
    for language in country['languages']:
        conteo[language] = conteo.get(language, 0) + 1

ordenados = sorted(conteo.items(), key=lambda par: par[1] , reverse=True)

top_ten = ordenados[:10]
print(top_ten)

# Find the 10 most populated countries in the world
ordenados = sorted(countries_data, key=lambda country: country['population'], reverse=True)
top_ten = ordenados[:10]

for country in top_ten:
    print(country['name'], country['population'])