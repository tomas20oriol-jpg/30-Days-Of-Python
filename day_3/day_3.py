age = int(22)
height = float(1.78)
complex_number = complex(2, 2)

base_of_triangle = float(input("Enter base: "))
height_of_triangle = float(input("Enter height: "))
area = base_of_triangle * height * 0.5
print('The area of the triangle is', area)

a = float(input('Enter side a: '))
b = float(input('Enter side b: '))
c = float(input('Enter side c: '))
perimeter = a + b + c
print('The perimeter of the triangle is', perimeter)

length = float(input('Enter length: '))
width = float(input('Enter width: '))
perimeter = 2*(length + width)
area = length*width
print('The area of the rectangle is', area)
print('The perimeter of the rectangle is', perimeter)

r = float(input('Get radius: '))
pi = 3.14
area = pi*r*r
circumference = 2*pi*r
print('The area of the circle is', area)
print('The circumference of the circle is', circumference)

# Given equation: y = 2x - 2
m1 = 2      # Slope
b = -2     # Y-intercept

# Calculate x-intercept (where y = 0)
x_intercept = -b / m1

print(f"Slope: {m1}")
print(f"Y-intercept: {b}")
print(f"X-intercept: {x_intercept}")   

# Find the slope and Euclidean distance between (2,2) 
# and point (6,10)
x1, y1 = 2, 2
x2, y2 = 6, 10
m2 = (y2-y1)/(x2-x1)
euclidean_distance = ((x2-x1)**2 + (y2-y1)**2)**0.5

# Compare the slopes 
if m1 > m2: 
    print('m1 > m2')
elif m1 == m2:
    print('m1 == m2')
else:
    print('m1 < m2')

# Calculate the value of y (y = x^2 + 6x + 9). 
# Try to use different x values and figure out 
# at what x value y is going to be 0.

def calculate_y(x):
    return x**2 + 6*x + 9

test_values = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
for x in test_values:
    y = calculate_y(x)
    print(f'x = {x}, y = {y}')

# Find the length of 'python' and 'dragon' and make a 
# falsy comparison statement.
print(len('python')!=len('dragon'))

# Use and operator to check if 'on' 
# is found in both 'python' and 'dragon'
print('on' in 'python' and 'on' in 'dragon')

# I hope this course is not full of jargon. 
# Use in operator to check if jargon is in the sentence.
sentence = 'I hope this course is not full of jargon'
print('jargon' in sentence)

# There is no 'on' in both dragon and python
print('on' not in 'pyhton' and 'on' not in 'dragon')

# Find the length of the text python and convert 
# the value to float and convert it to string
python = len('python')
python = float(python)
python = str(python)

# Even numbers are divisible by 2 and the remainder is zero. 
# How do you check if a number is even or not using python?
def check_if_even(number):
    if number % 2 == 0:
        return print('Even')
    else:
        return print('Uneven')
check_if_even(248)

# Check if the floor division of 7 by 3 is equal 
# to the int converted value of 2.7
print(7//3 == 2.7)

# Check if type of '10' is equal to type of 10
print(type('10')==type(10))

# Check if int('9.8') is equal to 10
print(int(9.8) == 10)

# Write a script that prompts the user to enter hours 
# and rate per hour. Calculate pay of the person?
hours = float(input('Enter hours: '))
rate_per_hour = float(input('Enter rate per hour: '))
print('Your weekly earning is', rate_per_hour*hours)

# Write a script that prompts the user to enter number 
# of years. Calculate the number of seconds a person can live. Assume a person can live hundred years
number_of_years = int(input('Enter number of years you have lived: '))
print(f'You have lived for {number_of_years*365*24*60*60}')

# Write a Python script that displays the following table