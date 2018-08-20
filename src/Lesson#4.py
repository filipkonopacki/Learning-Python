"""
Zadania kontrolne z czwartej lekcji podstaw Python, instrukcje warunkowe
"""
#zadanie1
print("**********Zadanie 1*********")
age = input("Podaj wiek: ")
try:
    age = float(age)
    if age >= 18:
        print("Jesteś pełnoletni")
    else:
        print("Jesteś niepełnoletni")
except ValueError:
    print("Podany ciąg nie jest liczbą!")

