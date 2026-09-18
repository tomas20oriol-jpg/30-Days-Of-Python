# Exercises: Day 13

# Filter only negative and zero in the list using list comprehension
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]

positive_numbers = [i for i in numbers if i > 0]
print(positive_numbers)

# Flatten the following list of lists of lists to a one dimensional list :
list_of_lists =[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
final_list = [number for row in list_of_lists for number in row]
print(final_list)

# Using list comprehension create the following list of tuples:
power_matrix = [(i, 1, i, i**2, i**3, i**4, i**5) for i in range(11)]
print(power_matrix)

# Flatten the following list to a new list:
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

output = [[country.upper(), country[:3].upper(), capital.upper()] 
          for sublist in countries 
          for country, capital in sublist]

print(output)

# Change the following list to a list of dictionaries:
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

output = [[{'country': country.upper(), 'city': capital.upper()}]
          for sublist in countries
          for country, capital in sublist]

print(output)

# Change the following list of lists to a list of concatenated strings:
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]

output = [name + ' ' + surname
          for sublist in names
          for name, surname in sublist]

print(output)

# Write a lambda function which can solve a slope or y-intercept of linear functions.
slope = lambda x1, y1, x2, y2: (y2 - y1) / (x2 - x1)

# Example: Find slope between (1, 2) and (3, 6)
m = slope(1, 2, 3, 6)
print(f"Slope (m): {m}")  # Output: 2.0