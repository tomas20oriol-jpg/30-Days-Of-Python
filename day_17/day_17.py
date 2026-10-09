# Exercises: Day 17
names = ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland', 'Estonia', 'Russia']

# Unpack the first five countries and store them in a variable nordic_countries, 
# store Estonia and Russia in es and ru respectively.
try:
    # Unpack the first five elements into nordic_countries, 
    # and the last two into es and ru
    *nordic_countries, es, ru = names
except Exception as e:
    print(e)
else:
    print('Nordic countries are:', nordic_countries)
    print('es:', es)
    print('ru:', ru)