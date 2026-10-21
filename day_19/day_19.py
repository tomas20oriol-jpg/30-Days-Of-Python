# Exercises: Day 19

# Write a function which count number of lines and number of words in a 
# text. All the files are in the data the folder:

# Read obama_speech.txt file and count number of lines and words
f = open('./data/obama_speech.txt')
obama_speech = f.read()

print(f'The number of lines in obama speech:', obama_speech.count('\n'))
print(f'The number of words in obama speech:', len(obama_speech.split()))

# Read michelle_obama_speech.txt file and count number of lines and words
f= open('./data/michelle_obama_speech.txt')
michelle_speech = f.read()

print(f'The number of lines in michelle obama speech:', michelle_speech.count('\n'))
print(f'The number of words in michelle obama speech:', len(michelle_speech.split()))

# Read donald_speech.txt file and count number of lines and words
f = open('./data/donald_speech.txt')
donald_speech = f.read()

print(f'The number of lines in Donald speech:', donald_speech.count('\n'))
print(f'The number of words in Donald speech:', len(donald_speech.split()))

# Read melina_trump_speech.txt file and count number of lines and words
f = open('./data/melina_trump_speech.txt')
melina_trump_speech = f.read()

print(f'The number of lines in Melina Trump speech:', melina_trump_speech.count('\n'))
print(f'The number of words in Melina Trump speech:', len(melina_trump_speech.split()))

# Read the countries_data.json data file in data directory, 
# create a function that finds the ten most spoken languages
from collections import Counter
import json

# Cambiamos json.loads() por json.load()



def most_spoken_languages(filename, limit=10):
  with open(filename, encoding='utf-8') as j:
    data = json.load(j)
  all_languages = [
      language for country in data for language in country.get('languages', [])
  ]
  return Counter(all_languages).most_common(limit)

print(most_spoken_languages(filename='./data/countries_data.json', limit=10))

# Read the countries_data.json data file in data directory, create a function that creates a list of the ten most populated countries
import json

def most_populated_countries(filename, limit=10):
    with open(filename, encoding='utf-8') as j:
        data = json.load(j)
        
    # Ordenar los países de mayor a menor población
    sorted_data = sorted(data, key=lambda x: x.get('population', 0), reverse=True)
    
    # Crear la lista con el formato exacto requerido
    return [
        {'country': c.get('name'), 'population': c.get('population', 0)}
        for c in sorted_data[:limit]
    ]

print(most_populated_countries(filename='./data/countries_data.json', limit=10))

# Exercises: Level 2
# Extract all incoming email addresses as a list from the email_exchange_big.txt file
import re

# 1. Abrir y leer el archivo de texto
with open('./data/email_exchanges_big.txt', 'r', encoding='utf-8') as f:
    lines = f.read()

# 2. Definir el patrón de expresión regular estándar del curso
pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

# 3. Encontrar todas las coincidencias y guardarlas en una lista
emails = re.findall(pattern, lines)

# 4. Mostrar el resultado
print(emails)

# Find the most common words in the English language. 
# Call the name of your function find_most_common_words, 
# it will take two parameters - a string or a file and a positive integer, 
# indicating the number of words. Your function will return an array of 
# tuples in descending order. Check the output
def find_most_common_words(filename, limit=10):
    with open(filename, encoding='utf-8') as f:
        data = f.read()

        # Find all words and convert them to lowercase
        words = re.findall(r'\b\w+\b', data.lower())

        # Count the words and use .most_common() instead of slicing
        words_counted = Counter(words)
        return words_counted.most_common(limit)
    
print(find_most_common_words(filename='./data/romeo_and_juliet.txt', limit=10))
    
# Use the function, find_most_common_words to find:
# 1. The ten most frequent words used in Obama's speech
print(find_most_common_words(filename='./data/obama_speech.txt', limit=10))

# 2. The ten most frequent words used in Michelle's speech
print(find_most_common_words(filename='./data/michelle_obama_speech.txt', limit=10))

# 3. The ten most frequent words used in Trump's speech
print(find_most_common_words(filename='./data/donald_speech.txt', limit=10))

# 4. The ten most frequent words used in Melina's speech
print(find_most_common_words(filename='./data/melina_trump_speech.txt', limit=10))

# Write a python application that checks similarity between two texts. 
# It takes a file or a string as a parameter and it will evaluate the 
# similarity of the two texts. For instance check the similarity between 
# the transcripts of Michelle's and Melina's speech. You may need a couple 
# of functions, function to clean the text(clean_text), function to remove 
# support words(remove_support_words) and finally to check the 
# similarity(check_text_similarity). List of stop words are in the data 
# directory
import re
from gensim.parsing.preprocessing import remove_stopwords
from difflib import SequenceMatcher

def clean_text(text):
    pattern = r'[^\w\s]'
    return re.sub(pattern, '', text)

def remove_support_words(text):
    # Usando gensim para remover stopwords (palabras de soporte)
    return remove_stopwords(text)

def check_text_similarity(source1, source2):
    # Soporta tanto archivos como strings directamente
    try:
        with open(source1, encoding='utf-8') as f:
            text1 = f.read()
    except OSError:
        text1 = source1

    try:
        with open(source2, encoding='utf-8') as f:
            text2 = f.read()
    except OSError:
        text2 = source2

    # Limpiar y quitar palabras de soporte para el primer texto
    clean_text1 = clean_text(text1)
    processed_text1 = remove_support_words(clean_text1)
    
    # Limpiar y quitar palabras de soporte para el segundo texto
    clean_text2 = clean_text(text2)
    processed_text2 = remove_support_words(clean_text2)
    
    # Evaluar similitud
    score = SequenceMatcher(None, processed_text1, processed_text2).ratio()
    return score

# Ejemplo de uso:
print(check_text_similarity('./data/michelle_obama_speech.txt', './data/melina_trump.txt'))

# Find the 10 most repeated words in the romeo_and_juliet.txt
print(find_most_common_words(filename='./data/romeo_and_juliet.txt', limit=10))

# Read the hacker news csv file and find out:
# Count the number of lines containing python or Python
def find_word(filename, word):
    with open(filename) as f:
       text = f.read()

    # Find all words and convert into lowercase
    lines = text.split('\n')
    line_counter = int(0)
    for line in lines:
        words = re.findall(r'\b\w+\b', line.lower())
        if word.lower() in words:
            line_counter += 1
    return line_counter

print(find_word(filename='./data/hacker_news.csv', word='Python'))

# Count the number lines containing JavaScript, javascript or Javascript
print(find_word(filename='./data/hacker_news.csv', word='JavaScript'))

# Count the number lines containing Java and not JavaScript
print(find_word(filename='./data/hacker_news.csv', word='Java'))

