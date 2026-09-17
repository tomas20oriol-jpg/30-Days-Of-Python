def generate_full_name(firstname, lastname):
    return firstname + ' ' + lastname

import random
import string

def random_user_id(length=6):
    characters = string.ascii_letters + string.digits
    return "".join(random.choices(characters, k=length))

def user_id_gen_by_user(length, number_IDs):
    characters = string.ascii_letters + string.digits
    user_id = list()
    for i in range(0, number_IDs):
        user_id.append("".join(random.choices(characters, k=length)))

    return user_id

def rgb_color_gen(length=1):
    rgb_list = []
    for i in range(0, length):
        primary_color = random.randint(0, 255)
        secondary_color = random.randint(0, 255)
        terciary_color = random.randint(0, 255)
        rgb_list.append(f'rgb({primary_color}, {secondary_color}, {terciary_color})')

    return rgb_list

def list_of_hexa_colors(length=1):
  hexa = '0123456789ABCDEF'
  hexa_list = []

  for i in range(0, length):
    # Add '#' here so each item in the list is a valid color string
    color = '#' + ''.join(random.choices(hexa, k=6))
    hexa_list.append(color)

  return hexa_list

def generate_colors(color, length_of_colors):
    if color.lower() == 'hexa':
        return list_of_hexa_colors(length_of_colors)
    elif color.lower() == 'rgb':
        return rgb_color_gen(length_of_colors)
    else:
        return 'Please give the correct color format.'

def shuffle_list(my_list):
    random.shuffle(my_list)
    return my_list
