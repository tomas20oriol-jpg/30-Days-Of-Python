# Exercises Day 8

# Create an empty dictionary called dog
dog = {}

# Add name, color, breed, legs, age to the dog dictionary
dog = {
    'name': 'Salomé',
    'breed': 'Maltese',
    'legs': 4,
    'age': 13,
}

# Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
student_dict = {
    'first_name': 'Tomas',
    'last_name': 'Oriol',
    'gender': 'Male',
    'age': 23,
    'marital_status': False,
    'skills': ['Python', 'Statistics', 'Feature Engineering', 'Data Science'],
    'country': 'Spain',
    'city': 'Barcelona',
    'adress': {
        'street': 'Calle Caja 1',
        'zipcode': '0901'
    }
}

# Get the length of the student dictionary
print('student dictionary length is:', len(student_dict))

# Get the value of skills and check the data type, it should be a list
print('value of skills:', student_dict['skills'])
print('data type of skills:', type(student_dict['skills']))

# Modify the skills values by adding one or two skills
student_dict['skills'].append('Patience')

# Get the dictionary keys as a list
keys = student_dict.keys()
print('keys are:', keys)

# Get the dictionary values as a list
values = student_dict.values()
print(values)

# Change the dictionary to a list of tuples using items() method
student_list = student_dict.items()
print(student_list)

# Delete one of the items in the dictionary
del student_dict['age']
print(student_dict)

# Delete one of the dictionaries
del student_dict