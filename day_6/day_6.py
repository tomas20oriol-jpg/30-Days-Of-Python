# Exercises Day 6
# Level 1

# Create an empty tuple
empty_tuple = tuple()

# Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
brothers = ('javier', 'nacho', 'pepe', 'luis')
sisters = ('maria', 'ana')

# Join brothers and sisters tuples and assign it to siblings
siblings = brothers + sisters

# How many siblings do you have?
print(f'I have {len(siblings)} siblings')

# Modify the siblings tuple and add the name of your father and mother and assign it to family_members
family_members = siblings + ('Nacho', 'Beth')

# Level 2

# Unpack siblings and parents from family_members
siblings = family_members[0:6]
parents = family_members[-2:]
print(siblings)
print(parents)

# Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
fruits = ('orange', 'apple', 'strawberry', 'banana')
vegetables = ('tomato', 'potato', 'carrot', 'onion')
animal = ('chicken', 'eggs', 'milk')
food_stuff_tp = fruits + vegetables + animal

# Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt = list(food_stuff_tp)

# Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
middle_item = food_stuff_tp[len(food_stuff_tp)//2]
print(f'Middle item is {middle_item}')

# Slice out the first three items and the last three items from food_stuff_lt list
first_three = food_stuff_lt[0:3]
print(f'First three items are {first_three}')

last_three = food_stuff_lt[-3:]
print(f'Last three items are {last_three}')

# Delete the food_stuff_tp tuple completely
del food_stuff_tp

# Check if an item exists in tuple:
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')

print('Is Estonia a nordic country?', 'Estonia' in nordic_countries)
print('Is Iceland a nordic country?', 'Iceland' in nordic_countries)