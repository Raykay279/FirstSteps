produkte = {
    "Klemme": 1.00,
    "Tetris": 2.00,
    "Bar": 3.00
}

gesamtpreis = 0

for produkt, preis in produkte.items():
    gesamtpreis += preis
    print(f"{produkt}: {preis:.2f}")

print(f"Gesamtpreis aller Prdukte: {gesamtpreis:.2f}")
