"""
    Program wywołany poleceniem python
        generator.py words_data animals_data
    zwraca na standardowe wyjście 10 proponowanych nazw zwierząt.
    
    Ideą tego prostego rozwiązania jest wzięcie 4 pierwszych liter losowego
    słowa z listy words i 2 ostatnich liter losowego zwierzęcia z listy animals.
    
    Można zobaczyć, że generowane nazwy są często słabe.
"""

import sys
import random


def read_data(filename):
    """
        Odczytuje dane z pliku filename.
        Zwraca listę słów.
    """
    with open(filename, 'r') as f:
        return f.read().split()
    
    
def generate_name(words, animals):
    """
        Generuje nazwę zwierzęcia.
        words – lista słów,
        animals – lista zwierząt.
    """
    return random.choice(words)[:4] + random.choice(animals)[2:]

words = read_data(sys.argv[1])
animals = read_data(sys.argv[2])
for i in range(10):
    print(generate_name(words, animals))
