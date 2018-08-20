"""
Zadania kontrolne z piątej lekcji podstaw Python, pętle
"""
#zadanie 1
import statistics
print("**********Zadanie 1**********")
match = [2, 3, 3.5, 4, 4.5, 5]
marks = []
while(True):
    try:
        mark = float(input("Podaj ocene: "))
        if mark not in match or mark is None: break
        marks.append(mark)
    except ValueError:
        "Podany ciąg nie jest cyfrą"
        break
if len(marks) != 0: print(f"Średnia ocen równa: {statistics.mean(marks)}")