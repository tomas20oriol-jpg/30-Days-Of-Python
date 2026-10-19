import re

# What is the most frequent word in the following paragraph?
paragraph = '''I love teaching. If you do not love teaching what else can you
love. I love Python if you do not love something which can give you all 
the capabilities to develop an application what else can you love.'''

palabras = re.findall(r'\b[a-zA-ZáéíóúÁÉÍÓÚñÑ]+\b', paragraph)

conteo = {}
for palabra in palabras:
    conteo[palabra] = conteo.get(palabra, 0) + 1

lista_resultado = []
for palabra, frecuencia in conteo.items():
    lista_resultado.append((palabra, frecuencia))

lista_resultado.sort(key=lambda x:x[0], reverse=True)

print(lista_resultado)

# The position of some particles on the horizontal x-axis are -12, -4, -3 
# and -1 in the negative direction, 0 at origin, 4 and 8 in the positive 
# direction. 
# Extract these numbers from this whole text and find the distance between 
# the two furthest particles.
text = '''The position of some particles on the horizontal x-axis are -12, 
-4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the 
positive direction. Extract these numbers from this whole text and find 
the distance between the two furthest particles.'''

points = re.findall(r'-?\d+(?:\.\d+)?', text)
sorted_points = [int(n) for n in points]
distance = sorted_points[-1] - sorted_points[0]
print(points)
print(sorted_points)
print(distance)

# Exercises: Level 2

# Write a pattern which identifies if a string is a valid python variable
import keyword
def is_valid_variable(variable: str):
    pattern = r'^[a-zA-Z_]\w*$'

    return bool(re.match(pattern, variable)) and not keyword.iskeyword(variable)

print(is_valid_variable("mi_variable"))  # True
print(is_valid_variable("_count"))       # True
print(is_valid_variable("2fast"))        # False (starts with a number)
print(is_valid_variable("if"))           # False (it's a reserved keyword)
print(is_valid_variable("hello-world"))  # False (contains a hyphen)

# Exercises: Level 3
sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. 
There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering 
peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. 
%Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''

clean_text = re.sub(r'[^a-zA-Z0-9\s]', '', sentence)
print(clean_text)

def most_frequent_words(paragraph: str) -> list:
    palabras = re.findall(r'\b[a-zA-ZáéíóúÁÉÍÓÚñÑ]+\b', paragraph)

    conteo = {}
    for palabra in palabras:
        conteo[palabra] = conteo.get(palabra, 0) + 1

    lista_resultado = []
    for palabra, frecuencia in conteo.items():
        lista_resultado.append((palabra, frecuencia))

    lista_resultado.sort(key=lambda x:x[0], reverse=True)
    return lista_resultado

print(most_frequent_words(clean_text))

