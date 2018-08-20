"""
                            Zadania laboratorium 4 Programowanie w językach skryptowych
Zadanie 1
    Napisz w języku Python program, który wczytuje tekst z pliku o nazwie podanej w argumencie i wyprowadza na
    stdout histogram częstości występowania liter alfabetu łacińskiego (litery małe i wielkie urożsamiamy). Histogram
    ma być posortowany w kolejności malejącej częstości wystąpień i może wyglądać np. tak:
A    2123    18.45%
E    1923    16,71%
:
:
"""
def zad1(file_name):
    hist = {}
    try:
        with open(path + file_name + '.txt') as file:
            for line in file:
                for n in line:
                    keys = hist.keys()
                    if(len(re.findall('\w',n)) != 0 and len(re.findall('\d',n)) == 0):
                        if n in keys:
                            hist[n] += 1
                        else:
                            hist[n] = 1
    except FileNotFoundError:
        print('Error')
    return hist
"""
Zadanie 2
    Dany jest plik, zawierający kolejno:
    -jedną linię, zawierającą 26 unikalnych wielkich liter alfabetu łacińskiego, odwzorowujących częstość występowania
    znaków w tekście otwartym  (znak występujący najczęściej jest pierwszy, najrzadziej - ostatni).
    -pewną, nieznaną z góry, liczbę linii tekstu zaszyfrowanego prostym szyfrem podstawieniowym, zachowującym rozkład
    częstości znaków określony w pierwszej linii.
Napisz skrypt w języku Python, który odszyfruje tekst.
"""
def zad2(file_name):
    hist = {}
    decoded_line = ""
    decoded_text = []
    try:
        with open(path + file_name + '.txt') as file:
            content = file.readlines()
            for n in content[0]:
                if(len(re.findall('\w',n)) != 0 and len(re.findall('\d',n)) == 0):
                    hist[n] = 1
            first_line = list(hist.keys())
            for line in content[1:]:
                for n in line:
                    if(hist.get(n) != None):
                        hist[n] += 1
            sorted_hist = dict(sorted(hist.items(), key=operator.itemgetter(1),reverse=True))
            pattern = list(sorted_hist.keys())
            for line in content[1:]:
                for n in line:
                    if(n in first_line):
                        decoded_line += pattern[first_line.index(n)]
                decoded_text.append(decoded_line[:])
                decoded_line = ''
            for txt in decoded_text:
                print(txt)

    except FileNotFoundError:
        print('Error')
    return hist


import operator
import re

path = 'C:/Users/filip/Documents/GitHub/Python/LearningPython/venv/Include/'
print('\t\t\t\tZadanie 1')
hist = zad1(input("Podaj nazwę pliku do wczytania (Tylko z folderu Input!): "))

for key, val in sorted(hist.items(), key=operator.itemgetter(1)):
    print(key, ": ", val, " ", round(val / sum(hist.values()) * 100, 2), "%")

print('\t\t\t\tZadanie 2')
zad2(input("Podaj nazwę pliku do wczytania (Tylko z folderu Input!): "))
