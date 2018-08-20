"""
Zadania kontrolne z szóstej lekcji podstaw Python, funkcje
"""
#zadanie 1

def number_to_text(numbers):
    result = ''
    for n in numbers:
        if(n in number_text):
            result += number_text[n] + ' '
    return result


number_text = {'0' : "zero", '1': "jeden", '2': "dwa", '3': "trzy", '4': "cztery", '5': "pięć", '6': "sześć", '7':"siedem", '8':"osiem", '9': "dziewięć"}
print("**********Zadanie 1**********")
numbers = input("Podaj liczbe: ");
print(number_to_text(numbers))