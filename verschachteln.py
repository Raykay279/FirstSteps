lagerbestand = [
    [5, 10, 15],       # Gruppe 1
    [3, 8, 6],         # Gruppe 2
    [12, 7, 4, 9]      # Gruppe 3
]

kategorienummer = 1
gesamtzahl = 0

for gruppe in lagerbestand:
    kategoriezahl = sum(gruppe)
    print(f"Kategorie {kategorienummer}  ist: {kategoriezahl}")
    kategorienummer += 1
    for menge in gruppe:
        gesamtzahl += menge

print("Gesamtzahl ist: ", gesamtzahl)

