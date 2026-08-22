# Exercises Day 7

# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# Level 1
# Find the length of the set it_companies
print(f'length of the set it_companies is {len(it_companies)}')

# Add 'Twitter' to it_companies
it_companies.add('Twitter')

# Insert multiple IT companies at once to the set it_companies
it_companies.update(['Samsung', 'Nvidia', 'ASML'])

# Remove one of the companies from the set it_companies
it_companies.remove('Twitter')

# What is the difference between remove and discard
'''They do the same but remove() does raise KeyError if the item is not on the set 
whereas discard does nothing'''

# Level 2
# Join A and B
C = A.union(B)

# Find A intersection B
intersection = A.intersection(B)

# Is A subset of B
A.issubset(B)

# Are A and B disjoint sets
A.isdisjoint(B)

# Join A with B and B with A
AB = A.union(B)
BA = B.union(A)

# What is the symmetric difference between A and B
A.symmetric_difference(B)

# Delete the sets completely
del A
del B

# Level 3
# Convert the ages to a set and compare the length of the 
# list and the set, which one is bigger?
age_st = set(age)
if len(age_st) > len(age):
    print('age set length is bigger to age list')
elif (len(age_st) < len(age)):
    print('age set length is smaller than age list')
else:
    print('age set length == age list length')

# I am a teacher and I love to inspire and teach people. 
# How many unique words have been used in the sentence? 
# Use the split methods and set to get the unique words.
sentence = 'I am a teacher and I love to inspire and teach people'
sentence = sentence.split()
unique_sentence = list(set(sentence))
print(f'The sentence has {len(unique_sentence)}')
