from my_module import generate_full_name, random_user_id, user_id_gen_by_user, rgb_color_gen, list_of_hexa_colors, generate_colors, shuffle_list

print(generate_full_name('Tomas', 'Oriol'))

# Exercises: Level 1
# Write a function which generates a six digit/character random_user_id
print(random_user_id())

# Modify the previous task. Declare a function named user_id_gen_by_user. 
# It doesn’t take any parameters but it takes two inputs using input(). 
# One of the inputs is the number of characters and the second input is the 
# number of IDs which are supposed to be generated.

print(
    user_id_gen_by_user(int(input('Enter number of characters: ')), 
    int(input('Enter number of IDs which are supposed to be generated: '))))

# Write a function named rgb_color_gen. 
# It will generate rgb colors (3 values ranging from 0 to 255 each).
print(rgb_color_gen())

# Exercises: Level 2
# Write a function list_of_hexa_colors which returns any number of hexadecimal
#  colors in an array (six hexadecimal numbers written after #. 
# Hexadecimal numeral system is made out of 16 symbols, 0-9 and first 6 letters
#  of the alphabet, a-f. Check the task 6 for output examples).
print(list_of_hexa_colors())

# Write a function list_of_rgb_colors which returns any number of RGB colors in an array.
print(generate_colors('hexa', 3))

# Exercises: Level 3
# Call your function shuffle_list, it takes a list as a parameter and it returns a shuffled list
print(shuffle_list([0, 1, 2, 3, 4, 5]))

# Write a function which returns an array of seven random numbers in a range of 0-9. 
# All the numbers must be unique.
