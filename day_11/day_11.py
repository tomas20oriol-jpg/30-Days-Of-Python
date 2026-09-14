# Exercises: Level 1
# Declare a function add_two_numbers. It takes two 
# parameters and it returns a sum.
def add_two_parameters(a: float, b: float) -> float:
    return a + b

num_a = float(input('Enter parameter a: '))
num_b = float(input('Enter parameter b: '))

result = add_two_parameters(num_a, num_b)
print(result)

# Area of a circle is calculated as follows: 
# area = π x r x r. Write a function that calculates
# area_of_circle
def area_of_circle(r: float) -> float:
    return 3.14*r*r

radius = float(input('Enter radius of circle: '))
result = area_of_circle(radius)
print(result)

# Write a function called add_all_nums which takes 
# arbitrary number of arguments and sums all the arguments.
# Check if all the list items are number types. 
# If not do give a reasonable feedback.
import numbers
def add_all_nums(*nums):
    for num in nums:
        if not isinstance(num, numbers.Number):
            return f'Error {num} is not a number. Please provide only numeric values'
    return sum(nums)

result = add_all_nums(2, 3, 5)

print(result)

# Temperature in °C can be converted to °F using this 
# formula: °F = (°C x 9/5) + 32. Write a function 
# which converts °C to °F, convert_celsius_to-fahrenheit.
def convert_celsius_to_fahrenheit(celsius: float) -> float:
    return celsius * 9/5 + 32

result = convert_celsius_to_fahrenheit(float(input('Enter Temperature in °C to convert into °F: ')))
print(result)

# Write a function called check-season, 
# it takes a month parameter and returns the season: 
# Autumn, Winter, Spring or Summer.
seasons = {
    'Autumn': [9, 10, 11],
    'Winter': [12, 1, 2],
    'Spring': [3, 4, 5],
    'Summer': [6, 7, 8]
}
def check_season(season: int) -> str:
    while season in range(1, 13):
        if season in seasons['Autumn']:
            return 'Autumn'
        elif season in seasons['Winter']:
            return 'Winter'
        elif season in seasons['Spring']:
            return 'Spring'
        else:
            return 'Summer'
    else:
        return f'The season {season} is not valid. Please provide a numeric value in the range in between 1 and 12.'

result = check_season(int(input('Enter a month of the year to get the season it belongs to: ')))
print(result)

# Write a function called calculate_slope which return 
# the slope of a linear equation.
def calculate_slope(equation):
    # First we remove all spaces and we normalize
    eq = equation.replace(" ", "").lower()

    # Is it a linear equation?
    if "**" in eq or "^" in eq:
        raise ValueError("Error: No es una ecuación lineal (tiene exponentes).")

    if "=" not in eq or "x" not in eq:
        raise ValueError("Error: Formato inválido.")

    # Split at '=' to get the right side
    right_side = eq.split("=")[1]
    # Split at 'x' to get the m_part
    m_part = right_side.split("x")[0]
    # Handle edge cases
    if m_part == '' or m_part == '+':
        return 1.0
    elif m_part == '-':
        return -1.0
    
    return float(m_part)

slope = calculate_slope(str(input('Enter linear equation to get slope: ')))
print(slope)

# Quadratic equation is calculated as follows: 
# ax² + bx + c = 0. Write a function which calculates 
# solution set of a quadratic equation, solve_quadratic_eqn.
def solve_quadratic_eqn(a: int, b: int, c: int) -> float:
    discriminate = (b**2 - 4*a*c)
    if discriminate < 0:
        return f'No real value exist as a solution to {a}x^2 + {b}x + {c} = 0'

    root = discriminate * 0.5
    x_1 = (-b + root)/(2*a)
    x_2 = (-b - root)/(2*a)
    return {x_1, x_2}

result = solve_quadratic_eqn(2, 3, 1)
print(result)

# Declare a function named print_list. It takes a list as a parameter 
# and it prints out each element of the list.
def print_list(lst):
    for item in lst:
        print(item)

print_list(['Tomas', 'Oriol', 'Freixa', 'Roca', 'Aurell'])

# Declare a function named reverse_list. It takes an array as a 
# parameter and it returns the reverse of the array (use loops).
def reverse_list(array):
    new_array = list()
    for i in range(len(array)-1,-1, -1):
        new_array.append(array[i]) 
    return new_array

result = reverse_list(['5', '4', '3', '2', '1'])
print(result)

# Declare a function named capitalize_list_items. 
# It takes a list as a parameter and it returns a capitalized list 
# of items 
def capitalize_list_items(lst):
    new_lst = list()
    for item in lst:
        item = item.upper()    
        new_lst.append(item)
    return new_lst

result = capitalize_list_items(['a', 'b', 'c'])
print(result)

# Declare a function named add_item. It takes a list and an item parameters.
#  It returns a list with the item added at the end.
def add_item(lst, item):
    lst.append(item)
    return lst

result = add_item(['1', '2'], '3')
print(result)

# Declare a function named remove_item. It takes a list and an item 
# parameters. It returns a list with the item removed from it.
def remove_item(lst, item):
    lst.remove(item)
    return lst

food_stuff = ['Potato', 'Tomato', 'Mango', 'Milk']
result = remove_item(food_stuff, 'Mango')
print(result)

# Declare a function named sum_of_numbers. It takes a number parameter 
# and it adds all the numbers in that range.
def sum_of_numbers(num):
    num_sum = 0
    for i in range(1, num+1):
        num_sum += i
    return num_sum

result = sum_of_numbers(100)
print(result)

# Declare a function named sum_of_odds. It takes a number parameter 
# and it adds all the odd numbers in that range.
def sum_of_odds(num: int) -> int:
    odd_sum = 0
    for i in range(1, num+1):
        if i % 2 == 0:
            pass
        else:
            odd_sum += i
    return odd_sum

result = sum_of_odds(5)
print(result)

# Declare a function named sum_of_even. It takes a number parameter 
# and it adds all the even numbers in that - range.
def sum_of_even(num: int) -> int:
    even_sum = 0
    for i in range(1, num+1):
        if i % 2 == 0:
            even_sum += i
    return even_sum

result = sum_of_even(5)
print(result)

# Exercises: Level 2

# Declare a function named evens_and_odds . It takes a positive integer 
# as parameter and it counts number of evens and odds in the number.
def evens_and_odds(integer: int) -> str:
    num_of_odds = 0
    num_of_evens = 0
    if integer <= 0:
        return f'The number provided cannot be {integer}. Please provide a positive integer.'
    for i in range(0, integer+1):
        if i % 2 != 0:
            num_of_odds += 1
        else:
            num_of_evens += 1
    return f'The number of odds are {num_of_odds}. \nThe number of evens are {num_of_evens}.'

result = evens_and_odds(100)
print(result)

# Call your function factorial, it takes a whole number as a parameter 
# and it return a factorial of the number
def factorial(num: int) -> int:
    num_fact = 1
    for i in range(1, num+1):
        num_fact = num_fact*i
    return num_fact

result = factorial(3)
print(result)

# Call your function is_empty, it takes a parameter and it checks if 
# it is empty or not
def is_empty(param):
    return not param

result = is_empty('')
print(result)

# Write different functions which take lists. They should calculate_mean, 
# calculate_median, calculate_mode, calculate_range, calculate_variance, 
# calculate_std (standard deviation).
def calculate_mean(lst) -> float:
    sum_lst = 0
    for i in lst:
        sum_lst += i
    return sum_lst/len(lst+1)

def calculate_median(lst) -> float: 
    sorted_list = sorted(lst)
    n = len(sorted_list)
    mid = n // 2
    if n % 2 == 0:
        return sorted_list[mid]
    else:
        return ((sorted_list[mid-1] + sorted_list[mid])/2)

result = calculate_median([1, 3, 5, 7, 9, 10])
print(result)

def calculate_mode(lst):
    if not lst:
        return "La lista está vacía"
        
    freq = {}
    for value in lst:
        freq[value] = freq.get(value, 0) + 1

    max_freq = max(freq.values())
    modas = [k for k, v in freq.items() if v == max_freq]

    if len(modas) == len(lst):
        return 'No hay modas, todos los valores son únicos'
    
    return modas[0] if len(modas) == 1 else modas

result = calculate_mode([4, 7, 4, 2, 7, 7, 9])
print(result)

def calculate_range(lst):
    max_range = max(lst)
    min_range = min(lst)
    return f'[{min_range},{max_range}]'

result = calculate_range([3, 2, 1, 5, 9])
print(result)

def calculate_variance(lst):
    mean = calculate_median(lst)
    N = len(lst)
    sum_values = 0
    for x in lst:
        sum_values += (x - mean)**2

    return sum_values/N

result = calculate_variance([2, 4, 4, 4, 5, 5, 7, 9])
print(result)

def calculate_std(lst):
    return calculate_variance(lst) ** 1/2

result = calculate_std([2, 4, 4, 4, 5, 5, 7, 9])
print(result)

# Write a function called greet which takes a default argument, name. 
# If no argument is supplied it should print "Hello, Guest!", 
# otherwise it should greet the person by name.

def greet(name):
    if is_empty(name) == True:
        return 'Hello, Guest!'
    return f'Hello, {name}!'

result = greet(input('Name: '))
print(result)

# Create a function called show_args to take an arbitrary number of named arguments 
# and print their names and values
def show_args(**kwargs):
    for name, value in kwargs.items():
        print(f"{name}: {value}")

# Write a function called is_prime, which checks if a number is prime   
def is_prime(num: int) -> bool:
    if num < 2:
        return False
    for i in range(2, num):
        if (num % i) == 0:
            return False
    return True

result = is_prime(int(input('Input a number to check if the number is prime: ')))
print(result)

# Write a functions which checks if all items are unique in the list.
def check_unique(items: list) -> bool:   
    seen = set()
    for item in items:
        if item in seen:
            return False
        seen.add(item)
    return True

result = check_unique([2, 4, 4, 4, 5, 5, 7, 9])
print(result)

# Write a function which checks if all the items of the list are of the same data type.
def check_dtype(items: list) -> bool:
    types_list = [type(item) for item in items]
    return (len(types_list) == len(set(types_list)))

result = check_dtype([1, "hola", 3.14])
print(result)

# Write a function which check if provided variable is a valid python variable
def is_valid_variable(name: str) -> bool:
    if not isinstance(name, str):
        return False
        
    keywords = {
        'False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 
        'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 
        'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 
        'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 
        'try', 'while', 'with', 'yield'
    }
    
    return name.isidentifier() and name not in keywords

print(is_valid_variable("my_variable"))

# Go to the data folder and access the countries-data.py file.
import sys
import os

# Add the parent directory (30-Days-Of-Python) to python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from data.countries_data import countries_data

# Create a function called the most_spoken_languages in the world. 
# It should return 10 or 20 most spoken languages in the world in descending order
def most_spoken_languages(countries):
    language_count = {}
    for country in countries:
        for language in country['languages']:
            language_count[language] = language_count.get(language, 0) + 1
    sorted_languages = sorted(language_count.items(), key= lambda item: item[1], reverse=True )
    return sorted_languages[:10]

result = most_spoken_languages(countries_data)
print(result)

# Create a function called the most_populated_countries. 
# It should return 10 or 20 most populated countries in descending order.
def most_populated_countries(countries):
    sorted_population = sorted(countries, key=lambda x: x['population'], reverse=True)
    return [{'country': c['name'], 'population': c['population']} for c in sorted_population[:10]]

result = most_populated_countries(countries_data)
print(result)