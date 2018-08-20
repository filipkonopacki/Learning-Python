"""
Zadania kontrolne z trzeciej lekcji podstaw Python, operatory
"""
#zadanie 1
print("**********Zadanie 1*********")
values = input("Wprowadź liczby po spacji: ")
values = values.split(" ")

for value in values:
    try:
        value = float(value)
    except ValueError:
        print(value, " nie jest liczbą")
        continue
    if (value%2) == 0:
        print(value, " to liczba parzysta")
    else:
        print(value, " to liczba nieparzysta")

print("*********Zadanie 2**********")
value = input("Podaj liczbe: ")
try:
    value = float(value)
    if (value % 1) == 0:
        print(value, " to liczba całkowita")
    else:
        print(value, " to liczba zmiennoprzecinkowa")
except ValueError:
    print("Podany ciąg nie jest liczbą!")

