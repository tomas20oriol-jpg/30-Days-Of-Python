# Concatenate 'Thirty', 'Days', 'Of', 'Python' into a single string with spaces
thirty = 'Thirty'
days = 'Days'
of = 'Of'
python = 'Python'
sentence1 = thirty + ' ' + days + ' ' + of + ' ' + python
print(sentence1)  # Output: Thirty Days Of Python

# Concatenate 'Coding', 'For', 'All' into a single string with spaces
coding = 'Coding'
for_word = 'For'  # Avoid using 'For' as a variable name (it's a keyword)
all_word = 'All'  # Same for 'All'
sentence2 = coding + ' ' + for_word + ' ' + all_word
print(sentence2)  # Output: Coding For All

# Declare a variable named company and assign it the value "Coding For All"
company = sentence2
print(company)    # Output: Coding For All   

# Print the length of the company string using len() 
# method and print().
length_of_company = len(company)
print(length_of_company)

# Change all the characters to uppercase letters 
# using upper() method.
company = company.upper()
print(company)

# Change all the characters to lowercase letters 
# using lower() method.
company = company.lower()
print(company)

# Use capitalize(), title(), swapcase() methods to format 
# the value of the string Coding For All.
company_capitalize = company.capitalize()
print(company_capitalize)
company_title = company.title()
print(company_title)
company_swapcase = company.swapcase()
print(company_swapcase)

# Cut(slice) out the first word of Coding For All string.
company_cut = company.split(maxsplit=1)[1]
print(company_cut)

company = "Coding For All"

# 1. Using the 'in' operator (Best for simple True/False checks)
print('Does it contain "Coding"?', 'Coding' in company)

# 2. Using find() 
# Returns the starting index if found (0), or -1 if not found.
print('Does it contain "Coding"?', company.find('Coding') != -1)

# 3. Using index() 
# Returns the starting index (0). Be careful: it raises a ValueError if the word is not found.
print('Index of "Coding":', company.index('Coding'))

# Replace the word coding in the string 'Coding For All' 
# to Python
new_company = company.replace('Coding', 'Python')
print(new_company)

# Change "Python for Everyone" to "Python for All" 
# using the replace method or other methods.
sentence1 = sentence1.replace('Everyone', 'All')
print(sentence1)

# Split the string 'Coding For All' using space as 
# the separator (split()) .
sentence2 = 'Coding For All'
result = sentence2.split(' ')
print(result)

# "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
#  split the string at the comma.
companies = 'Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon'
companies = companies.split(', ')
print(companies)

# What is the character at index 0 in the string 
# Coding For All.
print(sentence2[0])

# What is the last index of the string Coding For All.
print(sentence2[len(sentence2)-1])

# What character is at index 10 in "Coding For All" string
print(sentence2[10])

# Create an acronym or an abbreviation for the name 
# 'Python For Everyone'.
pfe = 'Python For Everyone'

# Create an acronym or an abbreviation for the name 
# 'Coding For All'.
cfa = 'Coding For All'

# Use index to determine the position of the 
# first occurrence of C in Coding For All.
index = cfa.index('C')
print(index)

# Use index to determine the position of the first 
# occurrence of F in Coding For All.
index = cfa.index('F')
print(index)

# Use rfind to determine the position of the last 
# occurrence of l in Coding For All People.
index = cfa.rfind('l')
print(index)

# Use index or find to find the position of the first 
# occurrence of the word 'because' in the following 
# sentence: 'You cannot end a sentence with because 
# because because is a conjunction'
sentence = 'You cannot end a sentence with because /n' \
'because because is a conjunction'
index = sentence.index('because')
print(index)

# Use rindex to find the position of the last occurrence 
# of the word because in the following sentence: 
# 'You cannot end a sentence with because because 
# because is a conjunction'
index = sentence.rfind('because')
print(index)

# Slice out the phrase 'because because because' 
# in the following sentence: 'You cannot end a sentence 
# with because because because is a conjunction'
first_index = sentence.index('because')
last_index = sentence.rfind('because') + len('because')
sentence = sentence[0:first_index] + sentence[last_index:]
sentence = sentence.replace("  ", " ")
print(sentence)

# Does 'Coding For All' start with a substring Coding?
cfa = 'Coding For All'
does_start = cfa.startswith('Coding')
print(does_start)

# Does 'Coding For All' end with a substring coding?
does_end = cfa.endswith('Coding')
print(does_end)

# '   Coding For All      '  , remove the left and right 
# trailing spaces in the given string.
cfa_2 = '   Coding For All      '
cfa_2 = cfa_2.replace("   ", "")
print(cfa_2)

# Which one of the following variables return True 
# when we use the method isidentifier():
# Starts with a number - Invalid identifier
print('30DaysOfPython'.isidentifier()) 
# Output: False

# Contains only letters and underscores, starts with a letter - Valid identifier
print('thirty_days_of_python'.isidentifier()) 
# Output: True

# The following list contains the names of some of python 
# libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 
# 'Falcon']. Join the list with a hash with space string.
libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']

# Join the list with a hash and a space
joined_string = '# '.join(libraries)

print(joined_string)

# Use the new line escape sequence to separate the 
# following sentences.
' I am enjoying this challenge. /n '
'I just wonder what is next. '

# Use a tab escape sequence to write the following lines.
# The '<' means left-align, and the number is the column width in characters
print(f"{'Name':<15} {'Age':<5} {'Country':<15} {'City':<15}")
print(f"{'Asabeneh':<15} {'250':<5} {'Finland':<15} {'Helsinki':<15}")

# Use the strin formatting method to display the following:
print(f'radius = {10}')
print(f'area = {3.14} * radius ** {2}')
print(f'The area of a circle with radius {10} is {3.14*10**2} meters square.')

# Make the following using string formatting methods:
a = 8
b = 6
print(f'{a} + {b} = {a+b}')
print(f'{a} - {b} = {a-b}')
print(f'{a} * {b} = {a*b}')
print(f'{a} / {b} = {a/b}')
print(f'{a} % {b} = {a%b}')
print(f'{a} // {b} = {a//b}')
print(f'{a} ** {b} = {a**b}')

