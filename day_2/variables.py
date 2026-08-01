# Exercises: Level 1

print("Day 2: 30 Days of python programming")

first_name = "Tomas"
last_name = "Oriol"
full_name = first_name + last_name
country = "Spain"
city = "Barcelona"
age = "22"
year = "2026"
is_married = "Not Married"
is_true, is_light_on = "True", "True"

# Exercises: Level 2

types = map(type, (first_name, last_name, full_name, country, 
                   city, age, year, is_married, is_true, is_light_on))

len(first_name)

len_first = len(first_name)
len_last = len(last_name)

if len_first == len_last:
    print("Equal length")
elif len_first > len_last:
    print("First name is longer")
else:
    print("Last name is longer")

num_one = 5
num_two = 4
diff = num_one-num_two
product = num_two*num_one
divison = num_one/num_two
remainder = num_two%num_one
exp = num_one**num_two
floor_division = num_one//num_two

r = 30
pi=3.14
area_of_circle = pi*r**2
circum_of_circle = 2*pi*r

r = input('Give me radius: ')
area_of_circle = pi*r**2
circum_of_circle = 2*pi*r

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
country = input("Enter your country: ")
age = int(input("Enter your age: "))

