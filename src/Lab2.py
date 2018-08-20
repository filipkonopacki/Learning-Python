"""
Problem
Tutaj i tutaj znajdują się strony z wynikami konkursu organizowanymi co roku przez nasz Wydział. Zakładamy, że dokumenty html
tych stron znajdują się w lokalnym systemie plików (np. zapisane przez przeglądarkę z użyciem operacji "Zapisz stronę jako...").
Twoim zadaniem jest napisanie skryptu parsującego takie pliki i wydobywającego z nich następujące informacje:

na ocenę 3.0: nazwę zawodnika (kolumna NAME) i liczbę punktów (kolumna SCORE)
na ocenę 4.0: nazwę zawodnika (kolumna NAME), nazwę konta użytkownika (zaszytą w kodzie HTML w kolumnie NAME) oraz liczbę punktów
z każdego zadania (zastąp kropkę dziesiętną przecinkiem, a pola zawierające '-' liczbą 0,0)
na ocenę 5.0: jak w przypadku oceny 4,0, ale dodatkowo wprowadź mechanizm wczytywania pliku tekstowego o nazwie przekazywanej
przez argument skryptu, zawierającego nazwy kont zawodników (po jednym w wierszu), którzy mają być uwzględnieni przy wyprowadzaniu
zestawienia; konta niewymienione w tym pliku są pomijane.

Plik html wczytuje się na z stdin, a uzyskany ekstrakt należy wyprowadzić na stdout w formacie CSV (z polami ograniczonymi
cudzysłowami i rozdzielonymi przecinkami)

Zwróć uwagę na fakt, że liczba kolumn tabeli wyników jest zmienna!

Uwaga: To jest zadanie na wyrażenia regularne! Ich użycie jest wymagane!
"""
import re
import sys
path = 'C:/Users/filip/Documents/GitHub/Python/LearningPython/venv/Include/'
file_name = input("Podaj nazwe pliku: ")
file = open(path + file_name, "r",encoding='UTF-8')
text = re.search("<tbody>(.*)<\/tr>",file.read()).group(0)
headers = list(filter(None,re.findall(">([A-Z0-9]*)<\/",
                    re.search(
                        "<tr class=\"headerrow\">(.*)<\/th></tr><tr class=\"problemrow\"",
                        text).group(0)
                    )))

scores = list(filter(None,re.search("<tr class=\"problemrow\">(.*)<\/tr>", text).group(0)\
    .split("<tr class=\"problemrow\">")))
nicknames = []
for row in range(len(scores)):

    scores[row] = scores[row].split("</td>")
    scores[row].remove("</tr>")
    nickname = re.search(
        "users\/(.*)\">", scores[row][1]
    )
    if nickname is not None:
        nicknames.append(
            nickname.group(0) \
                .replace("users/", "")
                .replace("\">", "")[:]
        )
    for record in range(len(scores[row])):
        scores[row][record] = scores[row][record].replace("<td class=\"mini\">","")
        try:
            scores[row][record] = re.search("\">(.*)<\/", scores[row][record]).group(0)
        except AttributeError:
            pass
        scores[row][record] = scores[row][record].replace(">", "")\
        .replace("</","").replace("\"", "").replace("-","0.0").replace(".",",")
print_cols = ("NAME", "SCORE", "WIPIN")
first_record = True
expected_nicknames = []
if (len(sys.argv) > 1):
    try:
        with open(sys.argv[1]) as file:
            for line in file:
                expected_nicknames.append(line.replace("\n",""))
    except FileNotFoundError:
        print('Error')
for row in range(len(scores)):
    if nicknames[row] in expected_nicknames or len(expected_nicknames) == 0:
        print("\""+nicknames[row]+"\"", end="")
        for column in range(len(headers)):
            for print_row in print_cols:
                if re.search(print_row, headers[column]) is not None:
                    print(",\"", end="")
                    print(scores[row][column], end="\"")
        print("")

