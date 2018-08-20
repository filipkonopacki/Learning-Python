"""
Zadania kontrolne z drugiej lekcji podstaw Python, złożone typy danych
"""
#zadanie pierwsze
print("**********Zadanie 1*********")
str = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua." \
      " Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat." \
      " Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur." \
      " Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
sentences = str.split(".")
for x in sentences[:-1]:
    print(len(x.split(" ")))

#zadanie 2
print("**********Zadanie 2*********")
def convert(number):
    return{
        "kilometers": int(number/1000),
        "miles": float(number/1608),
        "nautical miles": float(number/1852),
        "all": [int(number/1000),float(number/1608),float(number/1852)]
           }

distance = input("Podaj odległość w metrach: ")
convertedDistance = convert(float(distance))
print(convertedDistance)