# Exercises: Day 9

# Level 1
# 1
user_age = max(0, int(input('Enter your age: ')))
if user_age >= 18:
    print('You are old enough to learn to drive')
else:
    print(f'You need {18-user_age} more years to learn to drive')

# 2
my_age = 23
user_age = max(0, int(input('Enter your age: ')))
if user_age > my_age:
    print(f'You are {user_age-my_age} older than me')
elif user_age < my_age:
    print(f'You are {my_age-user_age} younger than me')
else:
    print('¡You have the same age as me!')

# 3 
a = float(input('Enter number one: '))
b = float(input('Enter number two: '))
if a > b:
    print(f'{a} is greater than {b}')
elif a < b:
    print(f'{a} is smaller than {b}')
else:
    print(f'{a} is equal to {b}')

# Level 2
# 1 
grade = max(0, float(input('Enter the student grade: ')))
if grade > 89:
    print('A')
elif grade > 79:
    print('B')
elif grade > 69:
    print('C')
elif grade > 59:
    print('D')
else:
    print('F')

# 2
Autumn = [9, 10, 11]
Winter = [12, 1, 2]
Spring = [3, 4, 5]
Summer = [6, 7, 8]

while True:
    try:
        user_month = int(input('Enter month (1-12): '))
        if 1 <= user_month <= 12:
            break  # Valid input, exit loop
        print("Invalid: Please enter a number between 1 and 12.")
    except ValueError:
        print("Invalid: Please enter a whole number.")

if user_month in Autumn:
    print('Autumn')
elif user_month in Winter:
    print('Winter')
elif user_month in Spring:
    print('Spring')
else:
    print('Summer')   

# 3

fruits = ['banana', 'orange', 'mango', 'lemon']
fruit = str(input('Enter new fruit: '))

if fruit not in fruits:
    fruits.append(fruit)
else:
    print('That fruit already exists in fruits')

# Level 3
person={
    'first_name': 'Tomas',
    'last_name': 'Oriol',
    'age': 23,
    'country': 'Spain',
    'is_married': False,
    'skills': ['Python', 'Data Science', 'Engineering', 'PowerBi'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

# * Check if the person dictionary has skills key,
#  if so print out the middle skill in the skills list.
if 'skills' in person:
    print('Skills is in person dictionary')
    middle_skill_index = len(person['skills']) // 2
    print(f'THe middle skill in person is {person['skills'][middle_skill_index]}')
else:
    print('Skills is not in person dictionary')

# * Check if the person dictionary has skills key, 
# if so check if the person has 'Python' skill and print 
# out the result.
if 'skills' in person:
    if 'Python' in person['skills']:
        print('The person has \'Python\' in skills')
    else:
        print('The person doesn\'t have \'Python\' in skills')
else:
    print('Skills is not in person dictionary')

# * If a person skills has only JavaScript and React, 
# print('He is a front end developer'), 
# if the person skills has Node, Python, MongoDB, 
# print('He is a backend developer'), 
# if the person skills has React, Node and MongoDB,
#  Print('He is a fullstack developer'), 
# else print('unknown title') - for more accurate results more conditions can be nested!

# * If the person is married and if he lives in Finland, print the information in the following format: