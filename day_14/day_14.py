countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Exercises: Level 1
# Explain de difference between map, filter and reduce

"""
- The map function is a built-in function that takes a function and 
iterable as parameters.

- The filter() function calls the specified function which returns boolean
for each item of the specified iterable (list). It filters the items that 
satisfy the filtering criteria.

- The reduce() function is defined in the functools module and we should
import it from this module. Like map and filter it takes two parameters, 
a function and an iterable. However, it does not return another iterable,
instead it returns a single value.
"""
# Explain the difference between higher order function, closure and decorator
"""
A higher-order function is any function that takes another function as an argument or returns one.

A closure is an inner function that retains access to variables from its outer function's scope even after the outer function has finished executing.

A decorator is a specialized higher-order function that wraps another function to modify or enhance its behavior.
"""

# Define a call function before map, filter or reduce, see examples.
## map

# Define the transformation function beforehand
def square(x):
    return x ** 2

# Pass the function name into map
squared_numbers = map(square, numbers)
print(list(squared_numbers))  # Output: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

## filter

# Define the filtering condition beforehand
def is_even(x):
    return x % 2 == 0

# Pass the function name into filter
even_numbers = filter(is_even, numbers)
print(list(even_numbers))  # Output: [2, 4, 6, 8, 10]

# Use for loop to print each country in the countries list
for country in countries:
    print(country)

# Use for to print each name in the names list.
for name in names:
    print(name)

# Use for to print each number in the numbers list
for number in  numbers:
    print(number)

# Exercises: Level 2
# Use map to create a new list by changing each country to uppercase in the countries list
def to_uppercase(country):
    return country.upper()

countries_uppercase  = map(to_uppercase, countries)

print(list(countries_uppercase))

# Use map to create a new list by changing each number to its square in 
# the numbers list
def square(num):
    return num**2

numbers_squared = map(square, numbers)

print(list(numbers_squared))

# Use map to change each name to uppercase in the names list
names_uppercase = map(to_uppercase, names)

print(list(names_uppercase))

# Use filter to filter out countries containing 'land'.
def contains_land(country):
    if 'land' in country:
        return True
    return False

land_countries = filter(contains_land, countries)
print(list(land_countries))

# Use filter to filter out countries having exactly six characters
def six_characters(country):
    if len(country) != 6:
        return True
    return False

six_characters_countries = filter(six_characters, countries)
print(list(six_characters_countries))

# Use filter to filter out countries containing six letters and more in the
# country list
def less_than_six(country):
    return len(country) < 6

short_countries = filter(less_than_six, countries)
print(list(short_countries))

# Use filter to filter out countries starting with an 'E'
def e_countries(country):
    if country.startswith('E'):
        return False
    return True

countries_filtered_e = filter(e_countries, countries)
print(list(countries_filtered_e))

# Chain two or more list iterators (eg. arr.map(callback).filter(callback).reduce(callback))
from functools import reduce

# 1. Define a reducer function (folds elements into a single value/sentence)
def concatenate_countries(acc, country):
    return f"{acc}, {country}"

# 2. Chain map -> filter -> reduce
countries_filtered = reduce(
    concatenate_countries,
    filter(six_characters, map(to_uppercase, countries))
)

print(countries_filtered)
# Output: ESTONIA, FINLAND, DENMARK, ICELAND

# Declare a function called get_string_lists which takes a list as a parameter
# and then returns a list containing only string items
def get_string_lists(lst):
    new_list = []
    for item in lst:
        if isinstance(item, str):
            new_list.append(item)
    return new_list

# Example usage:
mixed_list = [1, "apple", 3.14, "banana", True, "cherry"]
result = get_string_lists(mixed_list)
print(result)
# Output: ['apple', 'banana', 'cherry']

# Use reduce to sum all the numbers in the numbers list
total = reduce(lambda acc, x: acc + x, numbers)
print(total)

# Use reduce to concatenate all the countries and to produce this sentence: 
# Estonia, Finland, Sweden, Denmark, Norway, and Iceland are north European 
# countries
def join_countries(acc, country):
    if country == countries[-1]:
        return f'{acc}, and {country} are north European countries'
    return f'{acc}, {country}'

phrase_countries = reduce(join_countries, countries)

print(phrase_countries)

# Declare a function called categorize_countries that returns a list of 
# countries with some common pattern (you can find the countries list in this
#  repository as countries.js(eg 'land', 'ia', 'island', 'stan')).

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

# Alias so it doesn't overwrite the short countries list from above
from data.countries import countries as all_countries

def categorize_countries(countries: list, pattern: str) -> list:
    return list(filter(lambda country: pattern in country.lower(), countries))

for pattern in ['land', 'ia', 'island', 'stan']:
    print(f'{pattern}: {categorize_countries(all_countries, pattern)}')

# Create a function returning a dictionary, where keys stand for starting
# letters of countries and values are the number of country names starting
# with that letter.
def count_starting_letters(countries: list) -> dict:
    letters = {}
    for country in countries:
        first_letter = country[0]
        letters[first_letter] = letters.get(first_letter, 0) + 1
    return letters

print(count_starting_letters(all_countries))

# Declare a get_first_ten_countries function - it returns a list of first ten
# countries from the countries.js list in the data folder.
def get_first_ten_countries(countries: list) -> list:
    return countries[:10]

print(get_first_ten_countries(all_countries))

# Declare a get_last_ten_countries function that returns the last ten
# countries in the countries list.
def get_last_ten_countries(countries: list) -> list:
    return countries[-10:]

print(get_last_ten_countries(all_countries))

# Exercises: Level 3
# Use the countries_data.py file and follow the tasks below:
from data.countries_data import countries_data

# Sort countries by name, by capital, by population
by_name = sorted(countries_data, key=lambda country: country['name'])
by_capital = sorted(countries_data, key=lambda country: country['capital'])
by_population = sorted(countries_data, key=lambda country: country['population'])

print([country['name'] for country in by_name[:10]])
print([(country['name'], country['capital']) for country in by_capital[:10]])
print([(country['name'], country['population']) for country in by_population[:10]])

# Sort out the ten most spoken languages by location.
# (number of countries where each language is spoken)
languages_count = {}
for country in countries_data:
    for language in country['languages']:
        languages_count[language] = languages_count.get(language, 0) + 1

top_languages = sorted(languages_count.items(), key=lambda item: item[1], reverse=True)
print(top_languages[:10])

# Sort out the ten most populated countries.
most_populated = sorted(countries_data, key=lambda country: country['population'], reverse=True)
print([(country['name'], country['population']) for country in most_populated[:10]]) 