# Exercises Day 5
# Level 1

# Declare an empty list
empty_list = list()

# Declare a list with more than 5 items
items_list = ['item_1', 'item_2', 'item_3', 'item_4', 'item_5']
print(items_list)

# Find the length of your list
print('Length is:', len(items_list))

# Get the first item, the middle item and the last item of the list
first_item = items_list[0]
middle_item = items_list[len(items_list)//2]
last_item = items_list[-1]
print(f'first item: {first_item}, middle_item: {middle_item}, last_item: {last_item}')

# Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types = ['Tomas', 22, 178, 'not married', 'Calle Cajón 123']

# Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

# Print the list using print()
print(it_companies)

# Print the number of companies in the list
print('Length of it_companies is', len(it_companies))

# Print the first, middle and last company
first_company = it_companies[0]
middle_company = it_companies[len(it_companies)//2]
last_company = it_companies[-1]
print(f'First it company: {first_company}, Middle it company: {middle_company}, Last it company: {last_company}')

# Print the list after modifying one of the companies
it_companies[0] = 'Meta'
print(it_companies)

# Add an IT company to it_companies
it_companies.append('ASML')
print(it_companies)

# Insert an IT company in the middle of the companies list
it_companies.insert(len(it_companies)//2, 'Nvidia')
print(it_companies)

# Change one of the it_companies names to uppercase (IBM excluded!)
it_companies[0] = it_companies[0].upper()
print(it_companies)

# Join the it_companies with a string '#;  '
result = '#; '.join(it_companies)
print(result)

# Check if a certain company exists in the it_companies list.
def check_existence_it_company(company: str) -> None:  
    if (company in it_companies):
        print(f'{company} exists in it_companies.')
    else:
        print(f'{company} doesn\'t exist in it_companies')

check_existence_it_company(input('Input a company to check if it exists in it_companies: '))

# Sort the list using sort() method
it_companies.sort()
print(it_companies)

# Reverse the list in descending order using reverse() method
it_companies.reverse()
print(it_companies)

# Slice out the first 3 companies from the list
first_3_companies = it_companies[0:3]
print(first_3_companies)

# Slice out the last 3 companies from the list
last_3_companies = it_companies[-3:]
print(last_3_companies)
it_companies = it_companies[:-3]

# Slice out the middle IT company or companies from the list
it_companies = it_companies[: len(it_companies)//2 - 1] + it_companies[len(it_companies)//2 + 1:]
print(it_companies)

# Remove the first IT company from the list
del it_companies[0]

# Remove the middle IT company or companies from the list
del it_companies[len(it_companies)//2]

# Remove the last IT company from the list
del it_companies[-1]

# Remove all IT companies from the list
del it_companies[0:]

# Destroy the IT companies list
del it_companies

# Join the following lists:

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

full_stack = front_end + back_end

# After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack, then insert Python and SQL after Redux.#
full_stack.append('Python')
full_stack.append('SQL')
print(full_stack)

# Exercises Level 2

# The following is a list of 10 students ages:
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# Sort the list and find the min and max age
ages.sort()
min_age = ages[0]
max_age = ages[-1]
print(f'min age: {min_age}, max age: {max_age}')

# Add the min age and the max age again to the list
ages.append(min_age)
ages.append(max_age)
ages.sort()

# Find the median age (one middle item or two middle items divided by two)
median_age = ages[len(ages)//2]
print(median_age)

# Find the average age (sum of all items divided by their number )
avg_age = sum(ages)/len(ages)
print(avg_age)

# Find the range of the ages (max minus min)
range_ages = max_age - min_age
print(range_ages)

# Compare the value of (min - average) and (max - average), use abs() method
min_diff = abs(min_age - avg_age)
max_diff = abs(max_age - avg_age)

print(f"Absolute difference (min - average): {min_diff}")
print(f"Absolute difference (max - average): {max_diff}")

if min_diff > max_diff:
    print("The minimum age is further from the average than the maximum age.")
elif max_diff > min_diff:
    print("The maximum age is further from the average than the minimum age.")
else:
    print("The minimum and maximum ages are equally far from the average.")

# Find the middle country(ies) in the countries list
from data import countries

def get_middle_countries(country_list):
    n = len(country_list)
    
    # Handle empty list
    if n == 0:
        return []
        
    mid_index = n // 2
    
    # If the list length is even, return the two middle countries
    if n % 2 == 0:
        return [country_list[mid_index - 1], country_list[mid_index]]
    
    # If the list length is odd, return the single middle country
    else:
        return [country_list[mid_index]]

# Get and print the result
middle = get_middle_countries(countries)
print(f"Total countries: {len(countries)}")
print(f"Middle country(ies): {middle}")


# Divide the countries list into two equal lists if it is even if not one more country for the first half.
# ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Unpack the first three countries and the rest as scandic countries.